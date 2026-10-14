from __future__ import annotations

"""Render actual V3 DOCX packages page by page on CI; visual sign-off remains manual."""
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "arbeitsblaetter"
PREVIEWS = ROOT / "qa" / "3rd-round" / "pages"
DOCS = [
    ("A1_Text_formatieren.docx", 1),
    ("A7_Bilder_in_Word.docx", 1),
    ("ZUSATZ_Schnupperlehrbrief.docx", 1),
    ("START_Schnupperlehrbrief.docx", 1),
    ("ZUSATZ_Links_und_Quellen.docx", 1),
    ("START_Links_und_Quellen.docx", 1),
    ("lehrperson/MUSTER_Schnupperlehrbrief.docx", 1),
    ("lehrperson/MUSTER_Links_und_Quellen.docx", 1),
    ("lehrperson/LEHRPERSONENHILFEN_V3.docx", 4),
]


def _run(args: list[str], timeout=120) -> str:
    res = subprocess.run(args, check=True, text=True, capture_output=True, timeout=timeout)
    return res.stdout


def main() -> None:
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    for existing in PREVIEWS.glob("*.jpg"):
        existing.unlink()

    summary = []
    with tempfile.TemporaryDirectory(prefix="word-v3-render-") as td:
        work = Path(td)
        for rel, max_pages in DOCS:
            original = OUTPUT / rel
            if not original.is_file():
                raise RuntimeError(f"Missing DOCX for layout QA: {rel}")
            name = Path(rel).stem
            _run([
                "libreoffice", "-env:UserInstallation=file:///tmp/word-v3-qa-profile",
                "--headless", "--convert-to", "pdf", "--outdir", str(work), str(original)
            ])
            pdf = work / f"{name}.pdf"
            if not pdf.exists() or pdf.stat().st_size < 1000:
                raise RuntimeError(f"Failed PDF render: {rel}")
            details = _run(["pdfinfo", str(pdf)])
            matched = re.search(r"^Pages:\s*(\d+)", details, re.MULTILINE)
            if not matched:
                raise RuntimeError(f"No page count for {rel}")
            count = int(matched.group(1))
            if count < 1 or count > max_pages:
                raise RuntimeError(f"Unexpected pages for {rel}: {count}; expected 1..{max_pages}")
            basename = rel.replace("/", "__").replace(".docx", "")
            prefix = work / basename
            _run(["pdftoppm", "-f", "1", "-l", str(count), "-r", "105",
                  "-jpeg", "-jpegopt", "quality=82", str(pdf), str(prefix)])
            images = sorted(work.glob(f"{basename}-*.jpg"))
            if len(images) != count:
                raise RuntimeError(f"Missing preview images for {rel}")
            for page_index, image_file in enumerate(images, 1):
                with Image.open(image_file) as im:
                    w, h = im.size
                    if w < 650 or h < 850:
                        raise RuntimeError(f"Invalid preview dimensions {rel}: {w}x{h}")
                    im.convert("RGB").save(PREVIEWS / f"{basename}-p{page_index}.jpg",
                                           quality=82, optimize=True)
            summary.append({"docx": rel, "pages": count, "render": "LibreOffice + poppler"})
    manifest = {"status": "RENDERED_NOT_VISUALLY_APPROVED", "documents": summary,
                "native_word_365": "UNVERIFIED", "student_test": "UNVERIFIED"}
    (PREVIEWS.parent / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
