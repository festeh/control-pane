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
	let menuItems = $state<{ label: string; icon?: string; action: () => void }[]>([]);

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
				icon: 'terminal',
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
	<nav class="breadcrumb" aria-label="File path">
		<button class="crumb" onclick={() => navigate('/')} title="Root">
			<svg class="crumb-home" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
				<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
			</svg>
		</button>
		{#each breadcrumbSegments(currentPath) as seg, i}
			<span class="crumb-sep">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<path d="M9 18l6-6-6-6" />
				</svg>
			</span>
			<button class="crumb" onclick={() => navigate(seg.path)}>{seg.name}</button>
		{/each}
	</nav>

	{#if loading}
		<div class="loading-state">
			{#each Array(6) as _, i}
				<div class="skeleton-row" style="--i: {i}"></div>
			{/each}
		</div>
	{:else if error}
		<div class="error-state">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
				<circle cx="12" cy="12" r="10" />
				<line x1="15" y1="9" x2="9" y2="15" />
				<line x1="9" y1="9" x2="15" y2="15" />
			</svg>
			<span>{error}</span>
		</div>
	{:else}
		<div class="file-list">
			<button class="file-row file-row--dir" onclick={() => navigate(currentPath + '/..')}>
				<span class="file-icon">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
						<path d="M15 18l-6-6 6-6" />
					</svg>
				</span>
				<span class="file-name">..</span>
				<span class="file-size"></span>
			</button>
			{#each entries as entry, i}
				<button
					class="file-row"
					class:file-row--dir={entry.type === 'dir'}
					class:file-row--file={entry.type === 'file'}
					style="--i: {i}"
					onclick={() => entry.type === 'dir' ? navigate(`${currentPath}/${entry.name}`) : null}
					oncontextmenu={(e) => handleContextMenu(e, entry)}
				>
					<span class="file-icon">
						{#if entry.type === 'dir'}
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
								<path d="M2 6a2 2 0 0 1 2-2h5l2 2h9a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6z" />
							</svg>
						{:else}
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
								<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
								<path d="M14 2v6h6" />
							</svg>
						{/if}
					</span>
					<span class="file-name">{entry.name}</span>
					<span class="file-size">{entry.type === 'file' ? formatSize(entry.size) : ''}</span>
				</button>
			{/each}
		</div>
	{/if}
</div>

<ContextMenu bind:visible={menuVisible} x={menuX} y={menuY} items={menuItems} />

<style>
	.file-browser {
		margin-top: var(--space-2);
	}

	/* ═══ BREADCRUMB ═══ */
	.breadcrumb {
		display: flex;
		align-items: center;
		gap: var(--space-1);
		padding: var(--space-3) var(--space-4);
		background: var(--bg-elevated);
		border: 1px solid var(--border-subtle);
		border-radius: var(--radius-md);
		font-size: var(--text-sm);
		overflow-x: auto;
		scrollbar-width: none;
	}

	.breadcrumb::-webkit-scrollbar {
		display: none;
	}

	.crumb {
		padding: var(--space-1) var(--space-2);
		border-radius: var(--radius-sm);
		color: var(--text-secondary);
		font-size: var(--text-sm);
		font-weight: var(--weight-medium);
		white-space: nowrap;
		transition: all var(--duration-fast) var(--ease-out);
	}

	.crumb:hover {
		color: var(--accent-primary);
		background: var(--accent-primary-glow);
	}

	.crumb-home {
		width: 14px;
		height: 14px;
		display: block;
	}

	.crumb-sep {
		color: var(--text-tertiary);
		display: flex;
		align-items: center;
		flex-shrink: 0;
	}

	.crumb-sep svg {
		width: 12px;
		height: 12px;
	}

	/* ═══ LOADING ═══ */
	.loading-state {
		display: flex;
		flex-direction: column;
		gap: var(--space-2);
		padding: var(--space-4) 0;
	}

	.skeleton-row {
		height: 40px;
		border-radius: var(--radius-md);
		background: linear-gradient(
			90deg,
			var(--bg-elevated) 0%,
			var(--bg-overlay) 50%,
			var(--bg-elevated) 100%
		);
		background-size: 200% 100%;
		animation: shimmer 1.5s ease-in-out infinite;
		animation-delay: calc(var(--i) * 60ms);
		opacity: calc(1 - var(--i) * 0.12);
	}

	@keyframes shimmer {
		0% { background-position: 200% 0; }
		100% { background-position: -200% 0; }
	}

	/* ═══ ERROR ═══ */
	.error-state {
		display: flex;
		align-items: center;
		gap: var(--space-3);
		padding: var(--space-5);
		color: var(--danger);
		font-size: var(--text-sm);
	}

	.error-state svg {
		width: 20px;
		height: 20px;
		flex-shrink: 0;
	}

	/* ═══ FILE LIST ═══ */
	.file-list {
		display: flex;
		flex-direction: column;
		margin-top: var(--space-3);
		gap: 1px;
	}

	.file-row {
		display: flex;
		align-items: center;
		gap: var(--space-3);
		padding: var(--space-2) var(--space-3);
		border-radius: var(--radius-md);
		font-size: var(--text-sm);
		color: var(--text-secondary);
		transition: all var(--duration-fast) var(--ease-out);
		width: 100%;
		text-align: left;
		border: 1px solid transparent;
		cursor: default;
	}

	.file-row--dir {
		cursor: pointer;
	}

	.file-row--dir:hover {
		background: var(--bg-hover);
		border-color: var(--border-subtle);
		color: var(--text-primary);
	}

	.file-row--dir:hover .file-icon {
		color: var(--accent-primary);
	}

	.file-row--file:hover {
		background: var(--bg-hover);
	}

	.file-icon {
		width: 18px;
		height: 18px;
		flex-shrink: 0;
		color: var(--text-tertiary);
		transition: color var(--duration-fast) var(--ease-out);
	}

	.file-icon svg {
		width: 100%;
		height: 100%;
	}

	.file-row--dir .file-icon {
		color: var(--accent-secondary);
	}

	.file-name {
		flex: 1;
		min-width: 0;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.file-size {
		font-family: var(--font-mono);
		font-size: var(--text-xs);
		color: var(--text-tertiary);
		white-space: nowrap;
		flex-shrink: 0;
		min-width: 60px;
		text-align: right;
	}

	/* ═══ RESPONSIVE ═══ */
	@media (max-width: 768px) {
		.breadcrumb {
			padding: var(--space-2) var(--space-3);
		}

		.file-row {
			padding: var(--space-3) var(--space-2);
		}
	}
</style>
