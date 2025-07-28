import os
from flask import Flask, request, jsonify, send_from_directory, render_template
from gtts import gTTS
import PyPDF2
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'static/audio'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        return text

def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)

@app.route('/convert', methods=['POST'])
def convert():
    if 'pdfFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['pdfFile']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    pdf_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(pdf_path)

    try:
        text = pdf_to_text(pdf_path)
        output_file = os.path.join(AUDIO_FOLDER, 'audiobook.mp3')
        text_to_speech(text, output_file)
        return jsonify({'success': True, 'file_url': '/' + output_file})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)