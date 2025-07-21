/**
 * Screenshot capture functionality for dialoghelper
 * Provides persistent screen sharing with HTTP polling for screenshots
 */

let persistentStream = null;
let streamStatus = 'disconnected'; // 'disconnected', 'connecting', 'connected', 'error'

async function streamToBlob(stream, maxWidth = 512, maxHeight = 512) {
    return new Promise((resolve, reject) => {
        const video = document.createElement('video');
        video.srcObject = stream;
        video.muted = true;
        video.playsInline = true;
        video.addEventListener('loadedmetadata', () => {
            // Downscale to maxWidth x maxHeight using canvas
            const videoWidth = video.videoWidth;
            const videoHeight = video.videoHeight;
            const scaleX = maxWidth / videoWidth;
            const scaleY = maxHeight / videoHeight;
            const scale = Math.min(scaleX, scaleY, 1); // don't upscale
            const newWidth = Math.floor(videoWidth * scale);
            const newHeight = Math.floor(videoHeight * scale);
            const canvas = document.createElement('canvas');
            canvas.width = newWidth;
            canvas.height = newHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, newWidth, newHeight);
            canvas.toBlob(resolve, 'image/png');
        });
        video.addEventListener('error', reject);
        video.play().catch(reject);
    });
}

async function waitForGetDisplayMedia(timeout = 30000) {
    const start = Date.now();
    while (Date.now() - start < timeout) {
        if (navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia) { return true; }
        await new Promise(resolve => setTimeout(resolve, 100));
    }
    throw new Error('getDisplayMedia not available after timeout');
}


async function startPersistentScreenShare(statusId = null) {
		try {
				streamStatus = 'connecting';
				if (statusId) {
						fetch('/push_data_', {
								method: 'POST',
								headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
								body: new URLSearchParams({
										data_id: statusId,
										js_status: 'connecting'
								})
						});
				}
				await waitForGetDisplayMedia();
				persistentStream = await navigator.mediaDevices.getDisplayMedia({
						video: { mediaSource: 'screen', displaySurface: 'monitor' },
						audio: false
				});
				persistentStream.getVideoTracks()[0].addEventListener('ended', () => {
						console.log('Screen share ended by user');
						stopPersistentScreenShare();
				});
				streamStatus = 'connected';
				console.log('✅ Persistent screen share started');
				if (statusId) {
						fetch('/push_data_', {
								method: 'POST',
								headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
								body: new URLSearchParams({
										data_id: statusId,
										js_status: 'connected'
								})
						});
				}
				return { status: 'success', message: 'Screen share started' };
		} catch (error) {
				streamStatus = 'error';
				console.error('Failed to start persistent screen share:', error);
				if (statusId) {
						fetch('/push_data_', {
								method: 'POST',
								headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
								body: new URLSearchParams({
										data_id: statusId,
										js_status: 'error',
										error: error.message
								})
						});
				}
				return { status: 'error', message: error.message };
		}
}


function stopPersistentScreenShare() {
    if (persistentStream) {
        persistentStream.getTracks().forEach(track => track.stop());
        persistentStream = null;
    }
    streamStatus = 'disconnected';
    console.log('🛑 Persistent screen share stopped');
    return { status: 'success', message: 'Screen share stopped' };
}

function blobToBase64(blob) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
    });
}

async function processScreenshotBlob(blob, dataId) {
    const base64String = await blobToBase64(blob);
    const blob_type = blob.type || 'image/png';
    const b64data = base64String.split(',')[1]; // Remove the data URL prefix
    return { data_id: dataId, size: blob.size, img_type: blob_type, img_data: b64data };
}

async function captureScreenFromStream(dataId) {
    console.log("Executing screenshot from persistent stream");
    try {
        if (!persistentStream || streamStatus !== 'connected') {
            throw new Error('No active screen share. Call startPersistentScreenShare() first.');
        }
        const blob = await streamToBlob(persistentStream);
        const result = await processScreenshotBlob(blob, dataId);
        console.log("Screenshot result:", result);
        const pushResponse = await fetch('/push_data_', {
            method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(result)
        });
        if (pushResponse.ok) { console.log("✅ Screenshot data pushed to server"); }
				else { console.log("❌ Failed to push screenshot data"); }
    } catch (error) {
        console.error("Screenshot error:", error);
        await fetch('/push_data_', {
            method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ data_id: dataId, error: error.message })
        });
    }
    console.log("Finished executing screenshot");
}

window.startPersistentScreenShare = startPersistentScreenShare;
window.stopPersistentScreenShare = stopPersistentScreenShare;
window.captureScreenFromStream = captureScreenFromStream;
window.getStreamStatus = () => streamStatus;
