from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.static_folder = 'static'
app.debug = True

@app.route('/')
def waitListPage():
    return render_template('index.html')