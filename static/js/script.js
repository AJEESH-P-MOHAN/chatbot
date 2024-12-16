// Function to handle scrolling chat output
function handleChatScroll() {
    const chatOutput = document.getElementById('chatOutput');

    // Ensure the bottom of the scroll is visible
    chatOutput.scrollIntoView({ behavior: 'smooth', block: 'end'});
}

// Event listener for image upload
// Simply triggers the scroll functionality without showing a preview
document.getElementById('chatOutput').addEventListener('change', handleChatScroll);
