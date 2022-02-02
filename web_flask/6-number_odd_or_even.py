#!/usr/bin/python3
'''Module starts a Flask web app'''
from flask import Flask, render_template


app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    '''Function returns msg when web app is curled'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    '''Function returns msg when web app is curled'''
    return 'HBNB'


@app.route('/c/<text>')
def hello_c(text):
    '''Function returns msg when web app is curled'''
    return 'C ' + str(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def hello_python(text='is cool'):
    '''Function returns msg when web app is curled'''
    return 'Python ' + str(text).replace("_", " ")


@app.route('/number/<int:n>')
def hello_n(n):
    '''Function returns n if it's a number'''
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def hello_html1(n):
    '''Function returns html page if n is an int'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    '''Function returns odd or even'''
    num_status = 'even'
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               n=n, num_status=num_status)
    else:
        num_status = 'odd'
        return render_template('6-number_odd_or_even.html',
                               n=n, num_status=num_status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)