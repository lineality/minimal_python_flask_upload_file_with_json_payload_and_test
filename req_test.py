import requests
import json

# port server is running on
this_port = 5002  # Replace with the correct port number

item_a = "item_a"
item_b = "item_b"

# path to the file you want to upload
file_path = 'path/to/your/file.txt'
file_path = 'file.txt'

# Prepare the file in the correct format for uploading
file_bytes = {'file': open(file_path, 'rb')}

# Prepare your JSON data
json_payload = {'item_a': item_a, 'item_b': item_b}

# Convert JSON data to a string and include it in the form data
form_data = {
    'metadata': (None, json.dumps(json_payload)),  # 'None' as filename indicates this is not a file
    'file': file_bytes['file']
}

# Send the POST request to the server's file upload endpoint
r = requests.post(f'http://localhost:{this_port}/upload', files=form_data)

# Close the file after the request is made
file_bytes['file'].close()

# Print the server's response
print(r.text)


"""
// Possible nodejs code:
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

// Specify the port your Flask server is running on
const thisPort = 5000;  // Replace with the correct port number

// JSON payload
const jsonPayload = {
    item_a: "item_a",
    item_b: "item_b"
};

// Specify the path to the file you want to upload
const filePath = 'path/to/your/file.txt';

// Create an instance of FormData
const formData = new FormData();

// Append the file to the form data
formData.append('file', fs.createReadStream(filePath));

// Append the JSON payload as a string
formData.append('metadata', JSON.stringify(jsonPayload));

// Set the headers for the request
const headers = {
    ...formData.getHeaders()
};

// Send the POST request
axios.post(`http://localhost:${thisPort}/upload`, formData, { headers: headers })
    .then(response => {
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
"""
