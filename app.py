from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello! App is running. Build Number: {os.getenv('BUILD_ID', 'unknown')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
