from flask import Flask
import datetime
import os

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current_time

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
