import os
import socket
import subprocess
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

HOME_DIR = Path.home()


def resolve_safe(path_str: str) -> Path:
    """Resolve a path and ensure it stays within HOME_DIR."""
    resolved = Path(path_str).resolve()
    if not (resolved == HOME_DIR or HOME_DIR in resolved.parents):
        raise HTTPException(status_code=403, detail="Access denied: path outside home directory")
    return resolved


@app.get("/api/hostname")
def get_hostname():
    return {"hostname": socket.gethostname()}


@app.get("/api/files")
def list_files(path: str | None = None):
    dir_path = resolve_safe(path) if path else HOME_DIR

    if not dir_path.is_dir():
        raise HTTPException(status_code=400, detail="Not a directory")

    entries = []
    try:
        for entry in dir_path.iterdir():
            try:
                stat = entry.stat()
                entries.append({
                    "name": entry.name,
                    "type": "dir" if entry.is_dir() else "file",
                    "size": stat.st_size,
                    "modified": stat.st_mtime,
                })
            except (PermissionError, OSError):
                continue
    except PermissionError:
        raise HTTPException(status_code=403, detail="Permission denied")

    entries.sort(key=lambda e: (e["type"] != "dir", e["name"].lower()))

    return {"path": str(dir_path), "entries": entries}


class LaunchClaudeRequest(BaseModel):
    path: str


@app.post("/api/actions/launch-claude")
def launch_claude(req: LaunchClaudeRequest):
    dir_path = resolve_safe(req.path)

    if not dir_path.is_dir():
        raise HTTPException(status_code=400, detail="Not a directory")

    try:
        subprocess.Popen(
            ["claude"],
            cwd=str(dir_path),
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="claude CLI not found")

    return {"ok": True}
