from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBD66kXAuetdfBhg4839gQSEFv0-PdZ2Ug")
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('prompt')
        # Call your medical information generation logic here
        # For now, just returning a placeholder response
        return jsonify({'response': f'You asked about: {user_input}'})
        
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/medicines')
def medicines():
    return render_template('medicines.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('prompt')
    
    classify_prompt = f"""
    Is the following prompt health or medical related? Reply only with 'yes' or 'no'.

    Prompt: "{user_input}"
    """
    classification_response = model.generate_content(classify_prompt)
    classification = classification_response.text.strip().lower()

    
    if 'yes' in classification:
        medical_prompt = f"""
            Provide structured medical information for: "{user_input}"

            Use the following classes:
            - <h1 class="results-title"><br> for the title
            - <p class="result-description" style="margin-bottom: 0;"> for each paragraph
            - <ul class="list"><li class="item" style="margin-left: 20px;"> for lists
            - <p class="results-title"> for labels like "Causes", "Symptoms", etc.

            Do not wrap the response in triple backticks or markdown formatting.
        """

        medical_response = model.generate_content(medical_prompt)
        return jsonify({'response': medical_response.text})
    else:
        return jsonify({'response': 'I only provide medical advice.'})

if __name__ == '__main__':
    app.run(debug=True)
