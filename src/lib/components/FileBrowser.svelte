<script lang="ts">
	import { listFiles, launchClaude, type FileEntry } from '$lib/api';
	import ContextMenu from './ContextMenu.svelte';

	let currentPath = $state('');
	let entries = $state<FileEntry[]>([]);
	let loading = $state(true);
	let error = $state('');

	let menuVisible = $state(false);
	let menuX = $state(0);
	let menuY = $state(0);
	let menuItems = $state<{ label: string; action: () => void }[]>([]);

	async function navigate(path?: string) {
		loading = true;
		error = '';
		try {
			const res = await listFiles(path);
			currentPath = res.path;
			entries = res.entries;
		} catch (e) {
			error = e instanceof Error ? e.message : 'Failed to load files';
		} finally {
			loading = false;
		}
	}

	function handleContextMenu(e: MouseEvent, entry: FileEntry) {
		if (entry.type !== 'dir') return;
		e.preventDefault();
		menuX = e.clientX;
		menuY = e.clientY;
		const fullPath = `${currentPath}/${entry.name}`;
		menuItems = [
			{
				label: 'Launch in Claude Code',
				action: () => launchClaude(fullPath).catch((err) => alert(err.message))
			}
		];
		menuVisible = true;
	}

	function breadcrumbSegments(path: string): { name: string; path: string }[] {
		const parts = path.split('/').filter(Boolean);
		return parts.map((name, i) => ({
			name,
			path: '/' + parts.slice(0, i + 1).join('/')
		}));
	}

	function formatSize(bytes: number): string {
		if (bytes < 1024) return `${bytes} B`;
		if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
		return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
	}

	$effect(() => {
		navigate();
	});
</script>

<div class="file-browser">
	<nav class="breadcrumb">
		<button onclick={() => navigate('/')}>/ </button>
		{#each breadcrumbSegments(currentPath) as seg}
			<span class="sep">/</span>
			<button onclick={() => navigate(seg.path)}>{seg.name}</button>
		{/each}
	</nav>

	{#if loading}
		<p class="status">Loading...</p>
	{:else if error}
		<p class="status error">{error}</p>
	{:else}
		<table class="file-list">
			<thead>
				<tr>
					<th>Name</th>
					<th>Size</th>
				</tr>
			</thead>
			<tbody>
				<tr class="entry dir" onclick={() => navigate(currentPath + '/..')}>
					<td>
						<span class="icon">..</span>
					</td>
					<td></td>
				</tr>
				{#each entries as entry}
					<tr
						class="entry {entry.type}"
						onclick={() =>
							entry.type === 'dir' ? navigate(`${currentPath}/${entry.name}`) : null}
						oncontextmenu={(e) => handleContextMenu(e, entry)}
					>
						<td>
							<span class="icon">{entry.type === 'dir' ? '📁' : '📄'}</span>
							{entry.name}
						</td>
						<td class="size">{entry.type === 'file' ? formatSize(entry.size) : ''}</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/if}
</div>

<ContextMenu bind:visible={menuVisible} x={menuX} y={menuY} items={menuItems} />

<style>
	.file-browser {
		margin-top: 1rem;
	}

	.breadcrumb {
		display: flex;
		align-items: center;
		gap: 2px;
		padding: 8px 0;
		font-size: 0.875rem;
		flex-wrap: wrap;
	}

	.breadcrumb button {
		background: none;
		border: none;
		color: var(--link-color, #89b4fa);
		cursor: pointer;
		padding: 2px 4px;
		border-radius: 3px;
		font-size: 0.875rem;
	}

	.breadcrumb button:hover {
		background: var(--hover-bg, #313244);
	}

	.sep {
		color: var(--dim-text, #6c7086);
	}

	.status {
		padding: 1rem 0;
		color: var(--dim-text, #6c7086);
	}

	.status.error {
		color: var(--error-color, #f38ba8);
	}

	.file-list {
		width: 100%;
		border-collapse: collapse;
		font-size: 0.875rem;
	}

	.file-list th {
		text-align: left;
		padding: 6px 8px;
		border-bottom: 1px solid var(--border-color, #45475a);
		color: var(--dim-text, #6c7086);
		font-weight: 500;
	}

	.entry {
		cursor: default;
	}

	.entry.dir {
		cursor: pointer;
	}

	.entry td {
		padding: 4px 8px;
		border-bottom: 1px solid var(--border-color-subtle, #313244);
	}

	.entry:hover {
		background: var(--hover-bg, #1e1e2e);
	}

	.icon {
		margin-right: 6px;
	}

	.size {
		text-align: right;
		color: var(--dim-text, #6c7086);
		white-space: nowrap;
	}
</style>
