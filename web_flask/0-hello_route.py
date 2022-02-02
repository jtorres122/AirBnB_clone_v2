#!/usr/bin/python3
'''Module starts a Flask web app'''
from flask import Flask


app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    '''Function returns msg when web app is curled'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
