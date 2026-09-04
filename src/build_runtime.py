from __future__ import annotations

import os
import shutil
import tempfile
import zipfile
from contextlib import contextmanager
from pathlib import Path

from docx.document import Document as DocxDocument

_FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
_ORIGINAL_DOCX_SAVE = DocxDocument.save
_DOCX_SAVE_PATCHED = False


def resolve_font_paths() -> tuple[str, str]:
    """Return portable regular/bold sans-serif font paths for PIL previews.

    Optional environment overrides:
      WORD_KURS_FONT_REGULAR
      WORD_KURS_FONT_BOLD
    """
    env_regular = os.environ.get("WORD_KURS_FONT_REGULAR")
    env_bold = os.environ.get("WORD_KURS_FONT_BOLD")
    if env_regular and env_bold:
        regular = Path(env_regular).expanduser()
        bold = Path(env_bold).expanduser()
        if regular.is_file() and bold.is_file():
            return str(regular), str(bold)
        raise FileNotFoundError(
            "WORD_KURS_FONT_REGULAR / WORD_KURS_FONT_BOLD are set, "
            "but at least one path does not exist."
        )

    candidates = [
        (
            Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
            Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"),
        ),
        (
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ),
        (
            Path("C:/Windows/Fonts/arial.ttf"),
            Path("C:/Windows/Fonts/arialbd.ttf"),
        ),
        (
            Path("/Library/Fonts/Arial.ttf"),
            Path("/Library/Fonts/Arial Bold.ttf"),
        ),
        (
            Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
        ),
    ]
    for regular, bold in candidates:
        if regular.is_file() and bold.is_file():
            return str(regular), str(bold)

    raise FileNotFoundError(
        "No supported sans-serif font pair was found for PIL previews. "
        "Install Liberation Sans / DejaVu Sans, or set WORD_KURS_FONT_REGULAR "
        "and WORD_KURS_FONT_BOLD to existing TTF files."
    )


def _normalise_docx_zip(source: Path, destination: Path) -> None:
    """Rewrite a DOCX ZIP with stable entry order and timestamps."""
    with zipfile.ZipFile(source, "r") as zin, zipfile.ZipFile(
        destination,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zout:
        for name in sorted(zin.namelist()):
            original = zin.getinfo(name)
            info = zipfile.ZipInfo(filename=name, date_time=_FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = original.create_system
            info.external_attr = original.external_attr
            info.internal_attr = original.internal_attr
            info.comment = original.comment
            zout.writestr(info, zin.read(name), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def install_deterministic_docx_save() -> None:
    """Make path-based python-docx saves byte-stable across repeated builds."""
    global _DOCX_SAVE_PATCHED
    if _DOCX_SAVE_PATCHED:
        return

    def deterministic_save(self, file_or_stream):
        if hasattr(file_or_stream, "write"):
            return _ORIGINAL_DOCX_SAVE(self, file_or_stream)

        destination = Path(file_or_stream)
        destination.parent.mkdir(parents=True, exist_ok=True)
        raw_fd, raw_name = tempfile.mkstemp(prefix=".docx-raw-", suffix=".docx", dir=destination.parent)
        os.close(raw_fd)
        normal_fd, normal_name = tempfile.mkstemp(prefix=".docx-normal-", suffix=".docx", dir=destination.parent)
        os.close(normal_fd)
        raw = Path(raw_name)
        normal = Path(normal_name)
        try:
            _ORIGINAL_DOCX_SAVE(self, str(raw))
            _normalise_docx_zip(raw, normal)
            os.replace(normal, destination)
        finally:
            raw.unlink(missing_ok=True)
            normal.unlink(missing_ok=True)

    DocxDocument.save = deterministic_save
    _DOCX_SAVE_PATCHED = True


def _publish_directory(staged: Path, target: Path) -> None:
    if not staged.is_dir():
        raise RuntimeError(f"Staged output directory is missing: {staged}")

    backup = target.with_name(f".{target.name}.backup-{os.getpid()}")
    if backup.exists():
        shutil.rmtree(backup)

    target_was_present = target.exists()
    if target_was_present:
        os.replace(target, backup)

    try:
        os.replace(staged, target)
    except BaseException:
        if target.exists():
            shutil.rmtree(target)
        if target_was_present and backup.exists():
            os.replace(backup, target)
        raise
    else:
        if backup.exists():
            shutil.rmtree(backup)


@contextmanager
def staged_course_root(project_root: Path):
    """Build in a same-filesystem staging root and publish only on success."""
    project_root = Path(project_root)
    stage_root = Path(tempfile.mkdtemp(prefix=".word-kurs-build-", dir=project_root))
    try:
        yield stage_root
        _publish_directory(stage_root / "arbeitsblaetter", project_root / "arbeitsblaetter")
    finally:
        shutil.rmtree(stage_root, ignore_errors=True)
