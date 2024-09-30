import os
from flask import Flask, request, render_template
from legal_analysis import analyze_document  # Import the new analysis module

app = Flask(__name__)

# Create temp directory if it doesn't exist
if not os.path.exists('temp'):
    os.makedirs('temp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return render_template('index.html', error="No file part")
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error="No selected file")

    # Save the file to the temp directory
    file_path = os.path.join('temp', file.filename)
    file.save(file_path)

    # Analyze the document
    try:
        entities = analyze_document(file_path)
    except ValueError as e:
        return render_template('index.html', error=str(e))

    return render_template('result.html', entities=entities, filename=file.filename)

if __name__ == '__main__':
    app.run(debug=True)
