<script lang="ts">
	interface MenuItem {
		label: string;
		action: () => void;
	}

	let {
		x,
		y,
		items,
		visible = $bindable(false)
	}: { x: number; y: number; items: MenuItem[]; visible: boolean } = $props();

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Escape') visible = false;
	}

	function handleClickOutside() {
		visible = false;
	}
</script>

{#if visible}
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="backdrop" onmousedown={handleClickOutside} onkeydown={handleKeydown}>
		<!-- svelte-ignore a11y_no_static_element_interactions -->
		<div class="menu" style="left: {x}px; top: {y}px;" onmousedown={(e) => e.stopPropagation()}>
			{#each items as item}
				<button
					class="menu-item"
					onclick={() => {
						item.action();
						visible = false;
					}}
				>
					{item.label}
				</button>
			{/each}
		</div>
	</div>
{/if}

<style>
	.backdrop {
		position: fixed;
		inset: 0;
		z-index: 100;
	}

	.menu {
		position: fixed;
		background: var(--menu-bg, #1e1e2e);
		border: 1px solid var(--menu-border, #45475a);
		border-radius: 6px;
		padding: 4px 0;
		min-width: 180px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
	}

	.menu-item {
		display: block;
		width: 100%;
		padding: 6px 12px;
		border: none;
		background: none;
		color: var(--menu-text, #cdd6f4);
		font-size: 0.875rem;
		text-align: left;
		cursor: pointer;
	}

	.menu-item:hover {
		background: var(--menu-hover, #313244);
	}
</style>
