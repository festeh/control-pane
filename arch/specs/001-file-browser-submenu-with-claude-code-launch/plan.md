# Plan: File Browser with Claude Code Launch Action

**Spec**: arch/specs/001-file-browser-submenu-with-claude-code-launch/spec.md

## Tech Stack

- Language: TypeScript (frontend), Python (backend)
- Framework: SvelteKit 5 with Svelte 5 runes, FastAPI
- Storage: None (reads filesystem directly)
- Testing: None for now (minimal scaffold)

## Structure

New and changed files:

```
backend/
└── main.py                          # Add 2 endpoints: list files + launch claude
src/
├── lib/
│   ├── components/
│   │   ├── FileBrowser.svelte       # Main file browser: list + breadcrumbs
│   │   └── ContextMenu.svelte       # Right-click context menu
│   └── api.ts                       # Fetch helpers for backend calls
└── routes/
    └── +page.svelte                 # Mount FileBrowser on the main page
```

## Approach

### 1. Backend: List directory contents

Add `GET /api/files?path=/some/dir` to `main.py`.

- Use `pathlib.Path` to scan the directory.
- Return JSON array of entries: `{ name, type: "file"|"dir", size, modified }`.
- Sort: folders first, then files, alphabetical within each group.
- Default path: user's home directory.
- Guard against path traversal (resolve and check the path stays within allowed roots).

### 2. Backend: Launch Claude Code

Add `POST /api/actions/launch-claude` with body `{ "path": "/some/dir" }`.

- Validate the path exists and is a directory.
- Use `subprocess.Popen` to launch `claude` detached from the server process.
- Return `{ "ok": true }` on success or an error message on failure.

### 3. Frontend: API helpers

Create `src/lib/api.ts` with two functions:

- `listFiles(path: string)` — calls `GET /api/files?path=...`, returns entries.
- `launchClaude(path: string)` — calls `POST /api/actions/launch-claude`.

### 4. Frontend: FileBrowser component

Create `src/lib/components/FileBrowser.svelte`:

- State: `currentPath` (string), `entries` (array), `loading` (boolean).
- On mount and path change, fetch entries from the API.
- Render a breadcrumb bar from `currentPath` segments. Each segment is clickable.
- Render entries as a list/table. Folders are clickable to navigate. Each row shows an icon (📁/📄), name, size, and modified date.
- Right-click on a folder row opens the context menu.

### 5. Frontend: ContextMenu component

Create `src/lib/components/ContextMenu.svelte`:

- Props: `x`, `y` (position), `items` (array of `{ label, action }`), `visible`.
- Renders a positioned `<div>` at click coordinates.
- Closes on click outside or Escape key.
- For folders, show one item: "Launch in Claude Code" which calls `launchClaude(path)`.

### 6. Wire it up on the main page

Replace the current hostname-only page. Keep the hostname display, add the FileBrowser below it.

## Risks

- **Path traversal**: A crafted `path` param could access sensitive directories. Mitigation: validate and resolve paths, restrict to home directory or configurable root.
- **Process cleanup**: Launched Claude processes are detached and won't be tracked. Acceptable for now — this is a local dev tool, not a production service.

## Open Questions

- Should the file browser root be restricted to home directory, or allow browsing anywhere? (Default: home, for safety.)
