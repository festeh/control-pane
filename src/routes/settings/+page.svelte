<div class="settings-page">
	<header class="page-header">
		<h1 class="page-title">Settings</h1>
		<p class="page-subtitle">Configuration and preferences</p>
	</header>

	<div class="placeholder-card">
		<div class="placeholder-icon">
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
				<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6" />
			</svg>
		</div>
		<p class="placeholder-text">Settings coming soon</p>
		<p class="placeholder-hint">Configuration options will appear here</p>
	</div>
</div>

<style>
	.settings-page {
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

	.placeholder-card {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: var(--space-16) var(--space-8);
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		border-radius: var(--radius-lg);
		text-align: center;
	}

	.placeholder-icon {
		width: 48px;
		height: 48px;
		color: var(--text-tertiary);
		margin-bottom: var(--space-4);
		opacity: 0.4;
	}

	.placeholder-icon svg {
		width: 100%;
		height: 100%;
	}

	.placeholder-text {
		font-size: var(--text-md);
		font-weight: var(--weight-medium);
		color: var(--text-secondary);
		margin-bottom: var(--space-2);
	}

	.placeholder-hint {
		font-size: var(--text-sm);
		color: var(--text-tertiary);
	}
</style>
