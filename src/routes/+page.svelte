<script lang="ts">
  let hostname = $state('loading...');

  async function fetchHostname() {
    const res = await fetch('/api/hostname');
    const data = await res.json();
    hostname = data.hostname;
  }

  $effect(() => {
    fetchHostname();
  });
</script>

<h1>Control Pane</h1>
<p>Hostname: <strong>{hostname}</strong></p>
