# !pip install flask

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_index():
    return 'Test message. The server is running'
if __name__ == '__main__':
    app.run('localhost', 5000)
from server import *