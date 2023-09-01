from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current_time

if __name__ == '__main__':
    app.run(debug=True)