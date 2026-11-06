#!/usr/bin/env python3
"""Build one portable plugin; exclude the website and development materials."""
import argparse
from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "plugin.json", "LICENSE", "assets/icon.png",
    "skills/promptcraft-pro/SKILL.md",
    "skills/promptcraft-pro/agents/openai.yaml",
]

def build(destination):
    manifest = json.loads((ROOT / "plugin.json").read_text())
    assert manifest["name"] == ROOT.name
    assert not destination.resolve().is_relative_to(ROOT.resolve()), "Write the archive outside its source directory"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for relative in FILES:
            source = ROOT / relative
            assert source.is_file() and not source.is_symlink(), relative
            info = zipfile.ZipInfo(f"{manifest['name']}/{relative}", (2026, 11, 6, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    print(destination.resolve())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path)
    build(parser.parse_args().destination)
