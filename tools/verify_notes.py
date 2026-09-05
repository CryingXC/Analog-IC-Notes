#!/usr/bin/env python3
from pathlib import Path
import re, sys

FORBIDDEN_EXTS = {".gds", ".gdsii", ".oas", ".oasis", ".scs", ".dspf", ".spef", ".spf", ".tf"}
FORBIDDEN_DIRS = {"pdk", "models", "model", "rule_decks", "rules", "techfile", "extracted"}
MD_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

def verify(root: Path):
    errors = []
    for p in root.rglob("*"):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(root)
        parts_lower = {x.lower() for x in rel.parts}
        if p.is_dir() and parts_lower & FORBIDDEN_DIRS:
            errors.append(f"forbidden directory: {rel}")
        if p.is_file() and p.suffix.lower() in FORBIDDEN_EXTS:
            errors.append(f"forbidden extension: {rel}")
        if p.is_file() and p.suffix.lower() == ".md":
            text = p.read_text(encoding="utf-8")
            for target in MD_LINK.findall(text):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                candidate = (p.parent / target).resolve()
                try:
                    candidate.relative_to(root.resolve())
                except ValueError:
                    errors.append(f"link escapes repo: {rel} -> {target}")
                    continue
                if not candidate.exists():
                    errors.append(f"broken relative link: {rel} -> {target}")
    return errors

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = verify(root)
    if errors:
        print("Verification FAILED")
        for e in errors:
            print("-", e)
        return 1
    print("Verification PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
