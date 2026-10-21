document.querySelectorAll('video').forEach(video => {
    video.addEventListener('contextmenu', e => e.preventDefault());
});