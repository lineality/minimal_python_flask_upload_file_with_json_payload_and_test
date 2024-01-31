"""
When uploading files with an associated JSON payload, 
the content type of the request should be multipart/form-data, 
this means you can't *directly access the JSON payload using request.json. 
A common approach is to include the JSON data as a text string field 
in the multipart form data.

run with:
python app.py
"""
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import json  # Import json for parsing string to json

app = Flask(__name__)

# Configure the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads_should_be_here'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'docx'}

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint for uploading a single file along with a JSON payload."""
    # Check for file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    
    # Check if the file has a filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Optional: Handle JSON payload as a text field
    metadata = request.form.get('metadata', '{}')  # Default to empty JSON
    try:
        json_data = json.loads(metadata)  # Parse the JSON data
        
        # Extract json payload items (IRL: use real parameter names)
        item_a = json_data['item_a']
        item_b = json_data['item_b']
        
        # Test Pring
        print(json_data)
        print(item_a)
        print(item_b)
        
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    
    # Save file if it's allowed
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Return both file info and JSON data
        return jsonify({"message": "File uploaded successfully", 
        "filename": filename, 
        "metadata": json_data,
        }), 200
    else:
        return jsonify({"error": "File extension not allowed"}), 400

if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True, port=5002)  # Set debug=False in a production environment
