/**
 * Screenshot capture functionality for dialoghelper
 * Provides browser-based screen capture with solveit integration
 */

var isCapturing = false;

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
            const scale = Math.min(scaleX, scaleY, 1); // Don't upscale
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

async function captureScreen() {
    if (isCapturing) { throw new Error('Screenshot already in progress'); }
    isCapturing = true;
    try { // Request full monitor instead of window/tab
        const stream = await navigator.mediaDevices.getDisplayMedia({
            video: { mediaSource: 'screen', displaySurface: 'monitor' }, 
            audio: false,
        });
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

async function uploadScreenshotBlob(blob, sid) {
    const formData = new FormData();
    // Generate UUID following the same pattern as attachment_upload.js
    const imageid = crypto.randomUUID ? crypto.randomUUID() :
        'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            const r = Math.random() * 16 | 0;
            const v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    const filename = `pasted_image_${imageid}.png`;
    const dialogId = htmx.find('#full_editor input[name="did"]').value;
    console.log("Passed in sid:", sid);
    const msgId = sid;
    formData.append('file', new File([blob], filename, {type: blob.type}));
    formData.append('did', dialogId);
    formData.append('sid', msgId);
    formData.append('refresh_client', false); // default true behavior duplicates the edited msg on the client
    formData.append('return_data', true); // default behavior doesn't return image data
    console.log("Using sid:", msgId);
    const r = await fetch('/upload_attachment_', {method: 'POST', body: formData});
    if (r.status !== 200) {
        console.log('upload failed', r); 
        throw new Error(`Upload failed with status ${r.status}`);
    }
    let data;
    try {
        const responseText = await r.text();
        data = JSON.parse(responseText);
    } catch (e) {
        console.log('JSON parse error: response was not valid JSON');
        throw new Error('Invalid response from server');
    }
    const markdown_link = `![${filename}](attachment:${imageid})\n`;
    const base64String = await blobToBase64(blob);
    const blob_type = blob.type || 'image/png'; // default to png if type is not set
    const b64data = base64String.split(',')[1]; // get rid of url prefix "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
    return { imageid, filename, sid: sid, markdown: markdown_link, size: blob.size, img_type: blob_type, img_data: b64data};
}

async function captureScreenAndUpload(dataId) {
    console.log("Executing screenshot");
    try {
        const blob = await captureScreen();
        const result = await uploadScreenshotBlob(blob, dataId);
        console.log("Screenshot result:", result);
        const pushResponse = await fetch('/push_data_', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                data_id: dataId,
                data: JSON.stringify(result)
            })
        });
        if (pushResponse.ok) { console.log("✅ Screenshot data pushed to server"); } 
        else { console.log("❌ Failed to push screenshot data"); }
    } catch (error) {
        console.error("Screenshot error:", error);
        await fetch('/push_data_', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                data_id: dataId,
                data: JSON.stringify({ error: error.message })
            })
        });
    }
    console.log("Finished executing screenshot");
}

window.captureScreenAndUpload = captureScreenAndUpload;
