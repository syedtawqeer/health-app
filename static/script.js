// static/script.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('health-form');
    const userPromptInput = document.getElementById('user-prompt');
    const responseArea = document.getElementById('response-area');
    const submitButton = form.querySelector('button[type="submit"]');

    if (form && userPromptInput && responseArea && submitButton) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission

            const prompt = userPromptInput.value.trim();

            if (!prompt) {
                responseArea.innerHTML = '<div class="error-message">Please enter your symptoms or question.</div>';
                return;
            }

            // Show loading indicator
            responseArea.innerHTML = '<div class="loading-indicator"></div><p class="loading-text">Searching for information...</p>';
            submitButton.disabled = true; // Disable button during loading

            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ prompt: prompt })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.response || `HTTP error! status: ${response.status}`);
                }

                const result = await response.json();

                // Update the response area with the received HTML
                responseArea.innerHTML = result.response;

                // Optionally, you can add code here to find and process potential YouTube links
                // This would likely involve parsing the 'result.response' string for video URLs
                // and then embedding them or displaying thumbnails. This part would depend
                // heavily on the format of the YouTube links provided by the backend.

            } catch (error) {
                console.error('Fetch error:', error);
                responseArea.innerHTML = `<div class="error-message">An error occurred: ${error.message}. Please try again later.</div>`;
            } finally {
                submitButton.disabled = false; // Re-enable button
            }
        });
    } else {
        console.error("Required form elements not found.");
    }
});