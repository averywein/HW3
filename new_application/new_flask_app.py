#export FLASK_APP=new_flask_app.py
#python -m flask run

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/name')
def your_name():
	return render_template("name.html")

@app.route('/stores')
def pick_a_store():
	return render_template("stores.html")

@app.route('/shopping')
def text():
	return render_template("shopping.html")

if __name__ == '__main__':
    app.run()

