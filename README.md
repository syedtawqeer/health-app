# Health Information App

## Overview
This project is a web-based Health Information App that allows users to enter symptoms or health-related questions and receive structured medical information. The app uses Flask for the backend and integrates with Google's Gemini generative AI model to provide responses. The frontend is styled for a modern, user-friendly experience.

## Features
- **User Input:** Users can enter symptoms or health questions via a web form.
- **AI-Powered Responses:** The backend uses Google Gemini AI to classify and generate medical information.
- **Structured Output:** Responses are formatted with titles, paragraphs, and lists for clarity.
- **Error Handling:** User-friendly error messages and loading indicators.
- **Responsive Design:** The UI is mobile-friendly and visually appealing.

## Project Structure
```
health-app/
│
├── main.py                  # Flask backend, handles routes and AI integration
├── requirements.txt         # Python dependencies
├── static/
│   ├── script.js            # Frontend JavaScript for form handling and AJAX
│   └── style.css            # CSS for modern, responsive design
├── templates/
│   ├── home.html            # Main page with input form
│   └── health.html          # General health info page
│   └── ...                  # (Other HTML templates may be referenced in main.py)
└── devserver.sh             # (Optional) Development server script
```

## How It Works
1. **User Interaction:**
   - The user visits the home page and submits a health-related prompt.
   - JavaScript intercepts the form submission and sends the prompt to the `/ask` endpoint via AJAX.

2. **Backend Processing:**
   - The Flask backend receives the prompt and uses Gemini AI to check if the question is health-related.
   - If yes, Gemini generates a structured medical response, which is returned as HTML.
   - If not, the user is informed that only medical advice is provided.

3. **Frontend Display:**
   - The response is displayed in the `#response-area` div, styled for readability.

## Key Files
- **main.py:**
  - Defines Flask routes for home, health, and AI-powered `/ask` endpoint.
  - Integrates with Google Gemini AI for content generation.
- **static/script.js:**
  - Handles form submission, AJAX requests, and updates the UI with responses or errors.
- **static/style.css:**
  - Provides a clean, modern, and responsive look for the app.
- **templates/home.html:**
  - Main user interface with form and response area.
- **templates/health.html:**
  - Simple page for general health information.

## Setup Instructions
1. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the App:**
   ```sh
   python main.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Requirements
- Python 3.8+
- Flask
- google-generativeai
- gunicorn (for production, optional)

## Notes
- The app uses a Google Gemini API key (see `main.py`). Replace with your own key for production.
- Only health/medical-related prompts are processed.
- The app is for informational purposes and does not replace professional medical advice.

---

*Created June 2025.*
