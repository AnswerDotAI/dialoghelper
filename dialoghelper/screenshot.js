/**
 * Screenshot capture functionality for dialoghelper
 * Provides browser-based screen capture with solveit integration
 */

async function streamToBlob(stream, maxWidth = 512, maxHeight = 512) {
    return new Promise((resolve, reject) => {
        const video = document.createElement('video');
        video.srcObject = stream;
        video.muted = true;
        video.playsInline = true;
        video.addEventListener('loadedmetadata', () => {
            // Downscale to maxWith x maxHeight using canvas
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

var isCapturing = false;

async function waitForGetDisplayMedia(timeout = 30000) {
    const start = Date.now();
    while (Date.now() - start < timeout) {
        if (navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia) { return true; }
        await new Promise(resolve => setTimeout(resolve, 100));
    }
    throw new Error('getDisplayMedia not available after timeout');
}

async function captureScreen() {
    if (isCapturing) { throw new Error('Screenshot already in progress'); }
    isCapturing = true;
    try {
        await waitForGetDisplayMedia();
        const stream = await navigator.mediaDevices.getDisplayMedia({
            video: { mediaSource: 'screen', displaySurface: 'monitor' },  audio: false,});
        const blob = await streamToBlob(stream);
        stream.getTracks().forEach(track => track.stop());
        return blob;
    } finally { isCapturing = false; }
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

async function captureScreenAndUpload(dataId) {
    console.log("Executing screenshot");
    try {
        const blob = await captureScreen();
        const result = await processScreenshotBlob(blob, dataId);
        console.log("Screenshot result:", result);
        const pushResponse = await fetch('/push_data_', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(result)
        });
        if (pushResponse.ok) { console.log("✅ Screenshot data pushed to server"); } 
        else { console.log("❌ Failed to push screenshot data"); }
    } catch (error) {
        console.error("Screenshot error:", error);
        await fetch('/push_data_', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ data_id: dataId, error: error.message })
        });
    }
    console.log("Finished executing screenshot");
}

window.captureScreenAndUpload = captureScreenAndUpload;
