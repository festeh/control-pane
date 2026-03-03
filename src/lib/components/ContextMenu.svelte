<script lang="ts">
	interface MenuItem {
		label: string;
		icon?: string;
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

	const iconPaths: Record<string, string> = {
		terminal: 'M4 17l6-6-6-6M12 19h8'
	};
</script>

{#if visible}
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="backdrop" onmousedown={handleClickOutside} onkeydown={handleKeydown}>
		<!-- svelte-ignore a11y_no_static_element_interactions -->
		<div class="menu" style="left: {x}px; top: {y}px;" onmousedown={(e) => e.stopPropagation()}>
			<div class="menu-label">Actions</div>
			{#each items as item}
				<button
					class="menu-item"
					onclick={() => {
						item.action();
						visible = false;
					}}
				>
					{#if item.icon && iconPaths[item.icon]}
						<svg class="menu-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
							<path d={iconPaths[item.icon]} />
						</svg>
					{/if}
					<span>{item.label}</span>
				</button>
			{/each}
		</div>
	</div>
{/if}

<style>
	.backdrop {
		position: fixed;
		inset: 0;
		z-index: var(--z-modal);
	}

	.menu {
		position: fixed;
		background: var(--bg-elevated);
		border: 1px solid var(--border-default);
		border-radius: var(--radius-lg);
		padding: var(--space-1);
		min-width: 200px;
		box-shadow: var(--shadow-xl);
		animation: menuIn var(--duration-fast) var(--ease-out);
	}

	@keyframes menuIn {
		from {
			opacity: 0;
			transform: scale(0.95) translateY(-4px);
		}
		to {
			opacity: 1;
			transform: scale(1) translateY(0);
		}
	}

	.menu-label {
		font-family: var(--font-mono);
		font-size: var(--text-xs);
		font-weight: var(--weight-medium);
		letter-spacing: var(--tracking-widest);
		text-transform: uppercase;
		color: var(--text-tertiary);
		padding: var(--space-2) var(--space-3) var(--space-1);
	}

	.menu-item {
		display: flex;
		align-items: center;
		gap: var(--space-3);
		width: 100%;
		padding: var(--space-2) var(--space-3);
		border: none;
		background: none;
		color: var(--text-primary);
		font-size: var(--text-sm);
		font-weight: var(--weight-medium);
		text-align: left;
		cursor: pointer;
		border-radius: var(--radius-md);
		transition: all var(--duration-fast) var(--ease-out);
	}

	.menu-item:hover {
		background: var(--accent-primary-glow);
		color: var(--accent-primary);
	}

	.menu-item-icon {
		width: 16px;
		height: 16px;
		flex-shrink: 0;
	}
</style>
