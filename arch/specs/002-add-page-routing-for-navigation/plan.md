# Plan: Add Page Routing for Navigation

## Tech Stack

- Language: TypeScript (Svelte 5)
- Framework: SvelteKit (file-based routing)
- Testing: Manual (no test framework set up)

## Structure

Changes to existing files, plus new route directories:

```
src/
├── routes/
│   ├── +layout.svelte          # EDIT: remove activeNav state, pass nothing to Nav
│   ├── +page.svelte            # EDIT: keep as dashboard (status strip + quick actions + system summary)
│   ├── files/
│   │   └── +page.svelte        # NEW: full-page FileBrowser
│   ├── system/
│   │   └── +page.svelte        # NEW: system info page
│   └── settings/
│       └── +page.svelte        # NEW: settings page (placeholder)
├── lib/
│   └── components/
│       └── Nav.svelte          # EDIT: buttons → <a> tags, detect active from $page.url
```

## Approach

### 1. Convert Nav from state-driven to route-driven

Replace the `active` bindable prop with SvelteKit's `$page.url.pathname`. Change each nav item to have an `href` instead of an `id`. Swap `<button>` elements for `<a>` elements. Active state comes from comparing `$page.url.pathname` to the item's `href`.

Route mapping:
- `dashboard` → `/`
- `files` → `/files`
- `system` → `/system`
- `settings` → `/settings`

### 2. Simplify the layout

Remove `activeNav` state and `bind:active` from `+layout.svelte`. Nav becomes self-contained — it reads the URL on its own.

### 3. Keep dashboard as the root page

The current `+page.svelte` stays at `/`. Remove the FileBrowser card from it (that moves to `/files`). Keep: header with clock, status strip, quick actions, system summary card.

### 4. Create /files page

Move the FileBrowser component into a new `src/routes/files/+page.svelte`. Add a page header matching the dashboard style. The FileBrowser component stays unchanged.

### 5. Create /system page

New `src/routes/system/+page.svelte`. Expand the existing system info card into a full page. Fetch hostname from `/api/hostname`. Show platform, language, cores from `navigator`. Room to add more system details later.

### 6. Create /settings page

New `src/routes/settings/+page.svelte`. Placeholder page with header and "coming soon" message. Style it to match the dashboard aesthetic.

## Risks

- **Active state matching**: The root path `/` would partially match `/files`. Use exact match for `/` and `startsWith` for other paths.
- **Losing nav styles**: Changing `<button>` to `<a>` could break styles. Keep the same class names and add equivalent reset styles.

## Open Questions

None. The scope is clear and all pieces are in place.
