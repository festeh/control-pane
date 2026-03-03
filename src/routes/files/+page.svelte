<script lang="ts">
	import FileBrowser from '$lib/components/FileBrowser.svelte';
</script>

<div class="files-page">
	<header class="page-header">
		<h1 class="page-title">Files</h1>
		<p class="page-subtitle">Navigate filesystem, right-click folders to launch Claude Code</p>
	</header>

	<div class="browser-card">
		<FileBrowser />
	</div>
</div>

<style>
	.files-page {
		max-width: var(--content-max-width);
		animation: fadeIn var(--duration-slow) var(--ease-out);
	}

	@keyframes fadeIn {
		from { opacity: 0; transform: translateY(8px); }
		to { opacity: 1; transform: translateY(0); }
	}

	.page-header {
		margin-bottom: var(--space-6);
	}

	.page-title {
		font-size: var(--text-2xl);
		font-weight: var(--weight-black);
		letter-spacing: var(--tracking-tighter);
		margin-bottom: var(--space-1);
	}

	.page-subtitle {
		font-size: var(--text-sm);
		color: var(--text-tertiary);
	}

	.browser-card {
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		border-radius: var(--radius-lg);
		padding: var(--space-5);
		transition: border-color var(--duration-base) var(--ease-out),
		            box-shadow var(--duration-base) var(--ease-out);
	}

	.browser-card:hover {
		border-color: var(--border-default);
		box-shadow: var(--shadow-md);
	}
</style>
