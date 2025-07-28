# 📖 Audiobook Web App

A Flask-based web application that converts uploaded PDF documents into audiobooks using text-to-speech (TTS). It allows users to upload a PDF, extract its text, and listen to the generated audio.

---

## 🚀 Features

- 📄 Upload any PDF document.
- 🔊 Convert PDF text to audio using TTS.
- 🎧 Preview and download the generated audiobook (MP3).
- 🌐 Simple and responsive web interface built with HTML/CSS.

---

## 🖥 Project Structure

### pdf-to-audiobook/
│
### ├── app.py &nbsp;&nbsp;              # Main Flask backend
### ├── templates/
### │   └── index.html  &nbsp;&nbsp;        # Frontend HTML
### ├── static/
### │   └── audio/  &nbsp;&nbsp;           # Folder to store generated MP3s
### ├── uploads/ &nbsp;&nbsp;              # Folder to save uploaded PDFs
### ├── requirements.txt&nbsp;&nbsp;       # All Python dependencies
### └── README.md &nbsp;&nbsp;             # This file
---

## ⚙ Installation & Setup

### 1. Clone the Repository


git clone https:https://github.com/Keerthana12o/audiobook.git<br>
cd audiobook<br>
python -m venv venv<br>
source venv/bin/activate &nbsp;&nbsp;  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

---
### 2. Set Up the Environment (Optional but Recommended)

python -m venv venv <br>
source venv/bin/activate &nbsp;&nbsp;  # Windows: venv\Scripts\activate

---

### 3. Install Dependencies

 pip install -r requirements.txt

pip install Flask PyPDF2 gTTS

---


### ▶ Usage
### 1. Start the Server

python app.py

---

### 2. Open in Your Browser

http://127.0.0.1:5000

---

### 3. Upload & Convert

Upload a .pdf file

Click the convert button

Listen or download the MP3 🎧



