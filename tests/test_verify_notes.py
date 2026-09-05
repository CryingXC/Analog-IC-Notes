from pathlib import Path
import tempfile, importlib.util

spec = importlib.util.spec_from_file_location("verify_notes", Path(__file__).parents[1] / "tools" / "verify_notes.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_clean_repo_passes():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "README.md").write_text("[Doc](docs/a.md)", encoding="utf-8")
        (root / "docs").mkdir()
        (root / "docs/a.md").write_text("# A", encoding="utf-8")
        assert m.verify(root) == []

def test_broken_link_fails():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "README.md").write_text("[Missing](docs/no.md)", encoding="utf-8")
        assert any("broken relative link" in e for e in m.verify(root))

def test_foundry_like_file_fails():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "device.scs").write_text("model", encoding="utf-8")
        assert any("forbidden extension" in e for e in m.verify(root))

def test_forbidden_directory_fails():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "pdk").mkdir()
        assert any("forbidden directory" in e for e in m.verify(root))
