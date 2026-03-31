"""
VT Creator — Vojtech Titlbach consulting website
Flask app, port 5057
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='img', static_url_path='/img')

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weby')
def weby():
    return render_template('weby.html')

@app.route('/ai-automatizace')
def ai_automatizace():
    return render_template('ai_automatizace.html')

@app.route('/sluzby')
def sluzby():
    return render_template('sluzby.html')

@app.route('/ugc')
def ugc():
    return render_template('ugc.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

# Serve icons folder
@app.route('/icons/<path:filename>')
def icons(filename):
    return send_from_directory('icons', filename)

# Serve videos folder
@app.route('/videos/<path:filename>')
def videos(filename):
    return send_from_directory('videos', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5057, debug=True)
