// script.js
document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const imageInput = document.getElementById('imageInput');
    const loadingIndicator = document.getElementById('loading');

    uploadForm.addEventListener('submit', (e) => {
        if (imageInput.files.length === 0) {
            e.preventDefault();
            alert('Please select an image to upload.');
            return;
        }
        loadingIndicator.classList.remove('hidden');
    });
});
