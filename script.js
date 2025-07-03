function translateText() {
    const text = document.getElementById('inputText').value;
    const targetLanguage = document.getElementById('languageSelect').value;

    if (!text.trim()) {
        alert('Please enter text to translate!');
        return;
    }

    // Send a POST request to Flask backend
    fetch('http://localhost:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text,
            target_language: targetLanguage
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.translated_text) {
            document.getElementById('translatedText').innerText = data.translated_text;
        } else {
            document.getElementById('translatedText').innerText = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('translatedText').innerText = 'An error occurred during translation.';
    });
}
