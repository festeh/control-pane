<script lang="ts">
	let hostname = $state('...');

	async function fetchHostname() {
		const res = await fetch('/api/hostname');
		const data = await res.json();
		hostname = data.hostname;
	}

	$effect(() => {
		fetchHostname();
	});
</script>

<div class="system-page">
	<header class="page-header">
		<h1 class="page-title">System</h1>
		<p class="page-subtitle">Host information and runtime details</p>
	</header>

	<div class="info-grid">
		<div class="info-card">
			<span class="info-label">Hostname</span>
			<span class="info-value">{hostname}</span>
		</div>
		<div class="info-card">
			<span class="info-label">Platform</span>
			<span class="info-value">{navigator.platform || 'Unknown'}</span>
		</div>
		<div class="info-card">
			<span class="info-label">Language</span>
			<span class="info-value">{navigator.language}</span>
		</div>
		<div class="info-card">
			<span class="info-label">Cores</span>
			<span class="info-value">{navigator.hardwareConcurrency || '?'}</span>
		</div>
		<div class="info-card">
			<span class="info-label">User Agent</span>
			<span class="info-value info-value--small">{navigator.userAgent}</span>
		</div>
		<div class="info-card">
			<span class="info-label">Online</span>
			<span class="info-value info-value--status">
				<span class="status-dot"></span>
				{navigator.onLine ? 'Connected' : 'Offline'}
			</span>
		</div>
	</div>
</div>

<style>
	.system-page {
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

	.info-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--space-4);
	}

	.info-card {
		display: flex;
		flex-direction: column;
		gap: var(--space-2);
		padding: var(--space-5);
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		border-radius: var(--radius-lg);
		transition: border-color var(--duration-base) var(--ease-out),
		            box-shadow var(--duration-base) var(--ease-out);
		animation: cardIn var(--duration-slower) var(--ease-out) both;
		animation-delay: calc(var(--i, 0) * 60ms + 80ms);
	}

	.info-card:nth-child(1) { --i: 0; }
	.info-card:nth-child(2) { --i: 1; }
	.info-card:nth-child(3) { --i: 2; }
	.info-card:nth-child(4) { --i: 3; }
	.info-card:nth-child(5) { --i: 4; }
	.info-card:nth-child(6) { --i: 5; }

	@keyframes cardIn {
		from { opacity: 0; transform: translateY(12px); }
		to { opacity: 1; transform: translateY(0); }
	}

	.info-card:hover {
		border-color: var(--border-default);
		box-shadow: var(--shadow-md);
	}

	.info-label {
		font-family: var(--font-mono);
		font-size: var(--text-xs);
		font-weight: var(--weight-semibold);
		letter-spacing: var(--tracking-widest);
		text-transform: uppercase;
		color: var(--text-tertiary);
	}

	.info-value {
		font-size: var(--text-md);
		font-weight: var(--weight-medium);
		color: var(--text-primary);
		word-break: break-all;
	}

	.info-value--small {
		font-size: var(--text-xs);
		line-height: 1.5;
	}

	.info-value--status {
		display: flex;
		align-items: center;
		gap: var(--space-2);
	}

	.status-dot {
		width: 8px;
		height: 8px;
		border-radius: var(--radius-full);
		background: var(--success);
		box-shadow: 0 0 8px var(--success-dim);
	}

	@media (max-width: 768px) {
		.info-grid {
			grid-template-columns: 1fr;
		}
	}
</style>
