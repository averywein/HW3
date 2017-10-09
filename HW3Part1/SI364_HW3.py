## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

#export FLASK_APP=SI364_HW3.py
#python -m flask run

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/artistform')
def get_artist_form():
	return render_template("artistform.html")

@app.route('/artistinfo')
def get_artist_info():
	x = request.args
	pick_an_artist = x.get('artist')
	baseurl = "https://itunes.apple.com/search?term=" 
	url = baseurl + str(pick_an_artist)
	y = requests.get(url).text
	return render_template("artist_info.html", objects=json.loads(y)["results"])

@app.route('/artistlinks')
def artist_links():
    return render_template("artist_links.html")

@app.route('/specific/song/<artist_name>')
def artist_song(artist_name):
	baseurl = "https://itunes.apple.com/search?term=" 
	url = baseurl +str(artist_name)
	y = requests.get(url).text
	return render_template("specific_artist.html",
		results = json.loads(y)["results"])


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)
