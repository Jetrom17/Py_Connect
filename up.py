# up.py
from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

def is_directory(file_path):
    return os.path.isdir(file_path)

@app.route('/')
def index():
    files = os.listdir('.')
    return render_template('index.html', files=files, is_directory=is_directory)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

@app.route('/<path:filename>')
def serve_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    
    if os.path.isdir(file_path):
        files = os.listdir(file_path)
        return render_template('directory.html', files=files, folder_name=filename, is_directory=is_directory)
    else:
        return send_file(file_path)

@app.route('/download/<path:filename>')
def download_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='YOUR_IP_LAN')
