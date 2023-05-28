from flask import Flask, render_template
import requests
from stravalib import Client

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Strava activity viewer!"

@app.route('/activity/<activity_id>')
def activity(activity_id):
    # Initialize the Strava API client
    client = Client()

    # Set your Strava access token
    access_token = 'f72662ddfae723fa8d70cd5a1b76157bb5b0d7ea'
    client.access_token = access_token

    # Fetch the activity using its ID
    activity = client.get_activity(activity_id)

    # Fetch the segments for the activity
    segments = client.get_activity_segment_efforts(activity_id)

    return render_template('index.html', activity=activity, segments=segments)
