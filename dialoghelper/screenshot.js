document.body.addEventListener('shareScreen', async e => 
    window.vtrack = (await navigator.mediaDevices.getDisplayMedia()).getVideoTracks()[0]
);

window.getScreenshot = async (mxw=1280, mxh=1024) => {
    if (!window?.vtrack) return;
    const img = await new ImageCapture(window.vtrack).grabFrame();
    const scale = Math.min(mxw/img.width, mxh/img.height, 1);
    const c = document.createElement('canvas');
    [c.width, c.height] = [img.width*scale, img.height*scale].map(Math.floor);
    c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
    return c.toDataURL();
}

document.body.addEventListener('captureScreen', async e =>
    pushData(e.detail.idx, {img_data: await getScreenshot()})
);

