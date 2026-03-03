# Spec: File Browser with Claude Code Launch Action

## What

Add a file browser to the control panel that lists files and folders. Folders get a right-click context menu with a "Launch in Claude Code" action that opens Claude Code in that folder.

## Requirements

1. **File listing** — Browse directories on the server. Show files and folders with icons, names, and sizes. Click folders to navigate into them.
2. **Context menu** — Right-click a folder to see a submenu with custom actions.
3. **Launch in Claude Code** — Context menu action that starts `claude` CLI in the selected folder. Runs as a detached process on the server.
4. **Breadcrumb navigation** — Show the current path and allow clicking path segments to jump back.

## Out of Scope

- File upload/download
- File editing
- File deletion or rename
- Search
