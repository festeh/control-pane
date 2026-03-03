<script lang="ts">
	let currentTime = $state('');

	function updateTime() {
		const now = new Date();
		currentTime = now.toLocaleTimeString('en-US', {
			hour12: false,
			hour: '2-digit',
			minute: '2-digit',
			second: '2-digit'
		});
	}

	$effect(() => {
		updateTime();
		const interval = setInterval(updateTime, 1000);
		return () => clearInterval(interval);
	});
</script>

<div class="dashboard">
	<!-- Header -->
	<header class="dash-header">
		<div class="header-left">
			<h1 class="page-title">Dashboard</h1>
			<p class="page-subtitle">System overview and quick actions</p>
		</div>
		<div class="header-clock">
			<span class="clock-time">{currentTime}</span>
		</div>
	</header>

	<!-- Cards grid -->
	<div class="cards-grid">
		<!-- Files card -->
		<a class="card card-link" href="/files" style="--delay: 0;">
			<div class="card-header">
				<div class="card-icon">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
						<path d="M2 6a2 2 0 0 1 2-2h5l2 2h9a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6z" />
					</svg>
				</div>
				<div>
					<h2 class="card-title">Files</h2>
					<p class="card-desc">Browse filesystem and launch Claude Code</p>
				</div>
			</div>
		</a>

		<!-- Quick Actions card -->
		<div class="card card-actions" style="--delay: 1;">
			<div class="card-header">
				<div class="card-icon card-icon--amber">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
						<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
					</svg>
				</div>
				<div>
					<h2 class="card-title">Quick Actions</h2>
					<p class="card-desc">Common operations</p>
				</div>
			</div>
			<div class="card-body">
				<div class="actions-list">
					<button class="action-btn" onclick={() => {
						fetch('/api/actions/launch-claude', {
							method: 'POST',
							headers: { 'Content-Type': 'application/json' },
							body: JSON.stringify({ path: '~' })
						}).catch(() => {});
					}}>
						<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
							<path d="M4 17l6-6-6-6M12 19h8" />
						</svg>
						<div class="action-text">
							<span class="action-name">Launch Claude Code</span>
							<span class="action-hint">Open in home directory</span>
						</div>
					</button>
					<button class="action-btn" onclick={() => window.location.reload()}>
						<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
							<path d="M1 4v6h6M23 20v-6h-6" />
							<path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15" />
						</svg>
						<div class="action-text">
							<span class="action-name">Refresh</span>
							<span class="action-hint">Reload dashboard data</span>
						</div>
					</button>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.dashboard {
		max-width: var(--content-max-width);
		animation: fadeIn var(--duration-slow) var(--ease-out);
	}

	@keyframes fadeIn {
		from { opacity: 0; transform: translateY(8px); }
		to { opacity: 1; transform: translateY(0); }
	}

	/* ═══ HEADER ═══ */
	.dash-header {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
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

	.header-clock {
		text-align: right;
	}

	.clock-time {
		font-family: var(--font-mono);
		font-size: var(--text-lg);
		font-weight: var(--weight-medium);
		color: var(--accent-primary);
		letter-spacing: var(--tracking-wide);
		text-shadow: 0 0 20px var(--accent-primary-dim);
	}

	/* ═══ CARDS GRID ═══ */
	.cards-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--space-5);
		align-items: start;
	}

	.card {
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		border-radius: var(--radius-lg);
		overflow: hidden;
		transition: border-color var(--duration-base) var(--ease-out),
		            box-shadow var(--duration-base) var(--ease-out);
		animation: cardIn var(--duration-slower) var(--ease-out) both;
		animation-delay: calc(var(--delay, 0) * 80ms + 100ms);
	}

	@keyframes cardIn {
		from { opacity: 0; transform: translateY(12px); }
		to { opacity: 1; transform: translateY(0); }
	}

	.card:hover {
		border-color: var(--border-default);
		box-shadow: var(--shadow-md);
	}

	.card-link {
		text-decoration: none;
		color: inherit;
		cursor: pointer;
	}

	.card-header {
		display: flex;
		align-items: center;
		gap: var(--space-4);
		padding: var(--space-5) var(--space-5) var(--space-3);
	}

	.card-icon {
		width: 40px;
		height: 40px;
		padding: var(--space-2);
		border-radius: var(--radius-md);
		background: var(--accent-primary-glow);
		color: var(--accent-primary);
		flex-shrink: 0;
	}

	.card-icon--amber {
		background: var(--accent-secondary-dim);
		color: var(--accent-secondary);
	}

	.card-icon--purple {
		background: var(--accent-tertiary-dim);
		color: var(--accent-tertiary);
	}

	.card-icon svg {
		width: 100%;
		height: 100%;
	}

	.card-title {
		font-size: var(--text-md);
		font-weight: var(--weight-bold);
		margin-bottom: 2px;
	}

	.card-desc {
		font-size: var(--text-xs);
		color: var(--text-tertiary);
	}

	.card-body {
		padding: 0 var(--space-5) var(--space-5);
	}

	/* ═══ QUICK ACTIONS ═══ */
	.actions-list {
		display: flex;
		flex-direction: column;
		gap: var(--space-2);
	}

	.action-btn {
		display: flex;
		align-items: center;
		gap: var(--space-3);
		padding: var(--space-3) var(--space-4);
		border-radius: var(--radius-md);
		border: 1px solid var(--border-subtle);
		background: var(--bg-elevated);
		transition: all var(--duration-base) var(--ease-out);
		text-align: left;
		width: 100%;
	}

	.action-btn:hover {
		border-color: var(--accent-secondary);
		background: var(--bg-hover);
		box-shadow: 0 0 16px var(--accent-secondary-dim);
	}

	.action-btn svg {
		width: 18px;
		height: 18px;
		color: var(--accent-secondary);
		flex-shrink: 0;
	}

	.action-text {
		display: flex;
		flex-direction: column;
		gap: 2px;
	}

	.action-name {
		font-size: var(--text-sm);
		font-weight: var(--weight-medium);
		color: var(--text-primary);
	}

	.action-hint {
		font-size: var(--text-xs);
		color: var(--text-tertiary);
	}

	/* ═══ RESPONSIVE ═══ */
	@media (max-width: 768px) {
		.cards-grid {
			grid-template-columns: 1fr;
		}

		.dash-header {
			flex-direction: column;
			gap: var(--space-3);
		}

		.header-clock {
			text-align: left;
		}
	}
</style>
