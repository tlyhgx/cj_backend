from distutils.log import debug
from os import lseek
from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/hello')
def say_hello():
    return jsonify({"message":"hello world"})

if __name__=="__main__":
    app.run(debug=True)