<script lang="ts">
	import '$lib/styles/global.css';
	import favicon from '$lib/assets/favicon.svg';
	import Nav from '$lib/components/Nav.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Control Pane</title>
</svelte:head>

<div class="app-shell">
	<Nav />

	<main class="main-content">
		{@render children()}
	</main>
</div>

<style>
	.app-shell {
		min-height: 100dvh;
	}

	.main-content {
		margin-left: var(--nav-width);
		min-height: 100dvh;
		padding: var(--space-8) var(--space-8) var(--space-12);
	}

	@media (max-width: 768px) {
		.main-content {
			margin-left: 0;
			padding: var(--space-5) var(--space-4) calc(var(--mobile-nav-height) + var(--space-6));
		}
	}
</style>
