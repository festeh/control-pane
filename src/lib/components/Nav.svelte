<script lang="ts">
	interface NavItem {
		id: string;
		label: string;
		icon: string;
	}

	let { active = $bindable('dashboard') }: { active: string } = $props();

	const items: NavItem[] = [
		{ id: 'dashboard', label: 'Dashboard', icon: 'grid' },
		{ id: 'files', label: 'Files', icon: 'folder' },
		{ id: 'system', label: 'System', icon: 'cpu' },
		{ id: 'settings', label: 'Settings', icon: 'sliders' }
	];

	const iconPaths: Record<string, string> = {
		grid: 'M3 3h7v7H3zM14 3h7v7h-7zM3 14h7v7H3zM14 14h7v7h-7z',
		folder:
			'M2 6a2 2 0 0 1 2-2h5l2 2h9a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6z',
		cpu: 'M6 4h12v16H6zM2 9h4M2 15h4M18 9h4M18 15h4M9 1v3M15 1v3M9 20v3M15 20v3',
		sliders: 'M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6'
	};
</script>

<!-- Desktop sidebar -->
<nav class="sidebar" aria-label="Main navigation">
	<div class="sidebar-brand">
		<div class="brand-mark">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
				<rect x="3" y="3" width="18" height="18" rx="3" />
				<circle cx="12" cy="12" r="3" />
				<line x1="12" y1="3" x2="12" y2="9" />
				<line x1="12" y1="15" x2="12" y2="21" />
				<line x1="3" y1="12" x2="9" y2="12" />
				<line x1="15" y1="12" x2="21" y2="12" />
			</svg>
		</div>
		<span class="brand-text">CTRL PANE</span>
	</div>

	<div class="sidebar-items">
		{#each items as item}
			<button
				class="nav-item"
				class:active={active === item.id}
				onclick={() => (active = item.id)}
				aria-current={active === item.id ? 'page' : undefined}
			>
				<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
					<path d={iconPaths[item.icon]} />
				</svg>
				<span class="nav-label">{item.label}</span>
				{#if active === item.id}
					<span class="active-indicator"></span>
				{/if}
			</button>
		{/each}
	</div>

	<div class="sidebar-footer">
		<div class="status-dot"></div>
		<span class="status-text">System Online</span>
	</div>
</nav>

<!-- Mobile bottom bar -->
<nav class="bottombar" aria-label="Main navigation">
	{#each items as item}
		<button
			class="bottombar-item"
			class:active={active === item.id}
			onclick={() => (active = item.id)}
			aria-current={active === item.id ? 'page' : undefined}
		>
			<svg class="bottombar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
				<path d={iconPaths[item.icon]} />
			</svg>
			<span class="bottombar-label">{item.label}</span>
		</button>
	{/each}
</nav>

<style>
	/* ═══ DESKTOP SIDEBAR ═══ */
	.sidebar {
		position: fixed;
		top: 0;
		left: 0;
		bottom: 0;
		width: var(--nav-width);
		background: var(--bg-base);
		border-right: 1px solid var(--border-subtle);
		display: flex;
		flex-direction: column;
		z-index: var(--z-sticky);
		padding: var(--space-6) var(--space-3);
		gap: var(--space-2);
	}

	/* ── Brand ── */
	.sidebar-brand {
		display: flex;
		align-items: center;
		gap: var(--space-3);
		padding: var(--space-2) var(--space-3);
		margin-bottom: var(--space-6);
	}

	.brand-mark {
		width: 32px;
		height: 32px;
		color: var(--accent-primary);
		flex-shrink: 0;
	}

	.brand-mark svg {
		width: 100%;
		height: 100%;
	}

	.brand-text {
		font-family: var(--font-display);
		font-size: var(--text-sm);
		font-weight: var(--weight-black);
		letter-spacing: var(--tracking-widest);
		color: var(--text-primary);
	}

	/* ── Items ── */
	.sidebar-items {
		display: flex;
		flex-direction: column;
		gap: var(--space-1);
		flex: 1;
	}

	.nav-item {
		display: flex;
		align-items: center;
		gap: var(--space-3);
		padding: var(--space-3) var(--space-3);
		border-radius: var(--radius-md);
		color: var(--text-tertiary);
		font-size: var(--text-sm);
		font-weight: var(--weight-medium);
		transition: all var(--duration-base) var(--ease-out);
		position: relative;
		overflow: hidden;
	}

	.nav-item:hover {
		color: var(--text-secondary);
		background: var(--bg-hover);
	}

	.nav-item.active {
		color: var(--accent-primary);
		background: var(--accent-primary-glow);
	}

	.nav-icon {
		width: 20px;
		height: 20px;
		flex-shrink: 0;
	}

	.nav-label {
		white-space: nowrap;
	}

	.active-indicator {
		position: absolute;
		left: 0;
		top: 50%;
		transform: translateY(-50%);
		width: 3px;
		height: 20px;
		background: var(--accent-primary);
		border-radius: 0 var(--radius-full) var(--radius-full) 0;
	}

	/* ── Footer ── */
	.sidebar-footer {
		display: flex;
		align-items: center;
		gap: var(--space-2);
		padding: var(--space-3);
		border-top: 1px solid var(--border-subtle);
		margin-top: auto;
	}

	.status-dot {
		width: 8px;
		height: 8px;
		border-radius: var(--radius-full);
		background: var(--success);
		box-shadow: 0 0 8px var(--success-dim);
		animation: pulse 2s ease-in-out infinite;
	}

	.status-text {
		font-family: var(--font-mono);
		font-size: var(--text-xs);
		letter-spacing: var(--tracking-wide);
		text-transform: uppercase;
		color: var(--text-tertiary);
	}

	@keyframes pulse {
		0%, 100% { opacity: 1; }
		50% { opacity: 0.5; }
	}

	/* ═══ MOBILE BOTTOM BAR ═══ */
	.bottombar {
		display: none;
		position: fixed;
		bottom: 0;
		left: 0;
		right: 0;
		height: var(--mobile-nav-height);
		background: var(--bg-base);
		border-top: 1px solid var(--border-subtle);
		z-index: var(--z-sticky);
		padding: var(--space-2) var(--space-2) env(safe-area-inset-bottom, var(--space-2));
	}

	.bottombar-item {
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: var(--space-1);
		color: var(--text-tertiary);
		transition: color var(--duration-fast) var(--ease-out);
		padding: var(--space-1);
		border-radius: var(--radius-md);
	}

	.bottombar-item.active {
		color: var(--accent-primary);
	}

	.bottombar-item:hover {
		color: var(--text-secondary);
	}

	.bottombar-icon {
		width: 22px;
		height: 22px;
	}

	.bottombar-label {
		font-size: var(--text-xs);
		font-weight: var(--weight-medium);
		letter-spacing: var(--tracking-wide);
	}

	/* ═══ RESPONSIVE ═══ */
	@media (max-width: 768px) {
		.sidebar {
			display: none;
		}

		.bottombar {
			display: flex;
		}
	}
</style>
