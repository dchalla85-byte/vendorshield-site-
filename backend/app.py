from flask import Flask, request, jsonify
from utils.extractor import extract_text_from_pdf
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        text = extract_text_from_pdf(filepath)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
