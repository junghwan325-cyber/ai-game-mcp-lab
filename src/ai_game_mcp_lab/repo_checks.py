from __future__ import annotations

from pathlib import Path
import re

SECRET_PATTERN = re.compile(
    r"("
    r"(?:api[_-]?key|token|secret|oauth|cookie|password|client_secret)[ \t]*[:=][ \t]*['\"]?[^\s'\"#]+"
    r"|xox[baprs]-[A-Za-z0-9-]{8,}"
    r"|sk-[A-Za-z0-9_-]{16,}"
    r"|sk-ant-[A-Za-z0-9_-]{16,}"
    r")",
    re.IGNORECASE,
)

PRIVATE_PATH_FRAGMENTS = [
    "/home/" + "ubuntu",
    "/" + "root/",
    "/" + "srv/",
    "/" + "etc/caddy",
]


def text_files(root: str | Path):
    root = Path(root)
    ignored = {".git", "build", "exports", ".godot", "__pycache__", ".venv", "venv"}
    for path in root.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in {".glb", ".blend", ".png", ".jpg", ".jpeg", ".mp4", ".zip"}:
            continue
        yield path


def scan_secret_like_text(root: str | Path) -> list[str]:
    hits: list[str] = []
    root = Path(root)
    for path in text_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SECRET_PATTERN.search(text):
            hits.append(str(path.relative_to(root)))
    return hits


def scan_private_absolute_paths(root: str | Path) -> list[str]:
    hits: list[str] = []
    root = Path(root)
    for path in text_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(fragment in text for fragment in PRIVATE_PATH_FRAGMENTS):
            hits.append(str(path.relative_to(root)))
    return hits
