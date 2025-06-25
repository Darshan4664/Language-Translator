# Language-Translator
It was a mini project completed during my 6th semester

This is a simple, Language Translator Web App built using HTML, CSS, and JavaScript for the frontend and Flask (Python) with Googletrans for the backend. It translates text into multiple languages like Hindi, Gujarati, Spanish, and more using Google Translate API.

🚀 Features

🎯 Translate any input text to selected target languages
🌐 Supports multiple languages (e.g., English, Hindi, Gujarati, Spanish)
⚡ Instant and seamless translation
📱 Responsive and clean UI design
🔒 CORS enabled for frontend-backend communication

🧰 Technologies Used
Frontend
HTML5
CSS3 (Responsive Design)
JavaScript (Fetch API)

Backend
Python 3
Flask
Googletrans (Google Translate API wrapper)
Flask-CORS

📦 Installation and Setup
1. Clone the Repository
git clone https://github.com/Darshan4664/language-translator.git
cd language-translator

3. Create a Python Environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies
pip install flask googletrans==4.0.0-rc1 flask-cors

5. Run the Flask App
python app.py
Server will start at: http://localhost:5000

6. Open index.html in Browser
Simply double-click or serve the index.html file using any web server (or open it directly in your browser).

📄 How It Works
index.html: UI for input and output

script.js: Captures text and language selection, sends a POST request to the backend

app.py: Receives the request, translates the text using Google Translate, and returns the translated result

style.css: Adds a clean and responsive UI design

📝 Example
Input Text: Hello
Target Language: Hindi
Translated Text: नमस्ते


