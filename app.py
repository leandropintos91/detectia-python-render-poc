from flask import Flask
import datetime
import os
import requests

private_server_url = "http://detectia-backend-python:5000/"

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    # Make a GET request to the private server
    response = requests.get(private_server_url)

    if response.status_code == 200:
        # Successful response
        response_text = response.text  # Get the response text (a string)
        print("Response:", response_text)
        return response_text
    else:
        # Handle errors
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
