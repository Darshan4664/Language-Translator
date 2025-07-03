from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import translate_v2 as translate
import os

app = Flask(__name__)
CORS(app)

# Set your credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account.json"

translate_client = translate.Client()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text')
        target_language = data.get('target_language')

        if not text or not target_language:
            return jsonify({'error': 'Both text and target_language are required.'}), 400

        result = translate_client.translate(text, target_language=target_language)
        return jsonify({'translated_text': result['translatedText']})

    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
