export interface FileEntry {
	name: string;
	type: 'file' | 'dir';
	size: number;
	modified: number;
}

export interface FilesResponse {
	path: string;
	entries: FileEntry[];
}

export async function listFiles(path?: string): Promise<FilesResponse> {
	const params = path ? `?path=${encodeURIComponent(path)}` : '';
	const res = await fetch(`/api/files${params}`);
	if (!res.ok) throw new Error((await res.json()).detail ?? 'Failed to list files');
	return res.json();
}

export async function launchClaude(path: string): Promise<void> {
	const res = await fetch('/api/actions/launch-claude', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ path })
	});
	if (!res.ok) throw new Error((await res.json()).detail ?? 'Failed to launch Claude');
}
