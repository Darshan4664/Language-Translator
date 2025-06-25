from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text')  # Text to translate
        target_language = data.get('target_language')  # Target language code

        # Check if the target language is valid
        if target_language not in LANGUAGES:
            return jsonify({'error': f"Invalid target language: {target_language}."})

        # Translate the text
        translated = translator.translate(text, dest=target_language)

        # Return the translated text
        return jsonify({'translated_text': translated.text})
    
    except Exception as e:
        # Log the error and return it
        print(f"Error occurred: {str(e)}")
        return jsonify({'error': f"An error occurred during translation: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
