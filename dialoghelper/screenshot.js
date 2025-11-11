async function setupVideoStream() {
    vstream = await navigator.mediaDevices.getDisplayMedia();
    window.vtrack = vstream.getVideoTracks()[0];
}

async function getScreenshot(maxWidth = 1280, maxHeight = 1024) {
    if (window?.vtrack) {
        const cap = new ImageCapture(window.vtrack);
        const img = await cap.grabFrame();
        // rescale and convert to b64
        const scaleX = maxWidth / img.width;
        const scaleY = maxHeight / img.height;
        const scale = Math.min(scaleX, scaleY, 1); // don't upscale
        const newWidth = Math.floor(img.width * scale);
        const newHeight = Math.floor(img.height * scale);
        const c = document.createElement('canvas');
        c.width = newWidth; c.height = newHeight;
        c.getContext('2d').drawImage(img, 0, 0, newWidth, newHeight);
        return c.toDataURL();
    }
}

function pushData(dataId, data) {
    return fetch('/push_data_blocking_', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({data_id: dataId, ...data})
    });
}

window.setupVideoStream = setupVideoStream;
window.getScreenshot = getScreenshot;
window.pushData = pushData;