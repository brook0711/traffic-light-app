from flask import Flask, jsonify, render_template
import time

app = Flask(__name__)

green = 30
yellow = 5
red = 25
cycle = green + yellow + red

def get_light():
    current = int(time.time()) % cycle

    if current < green:
        return {"light": "green", "remain": green - current}
    elif current < green + yellow:
        return {"light": "yellow", "remain": green + yellow - current}
    else:
        return {"light": "red", "remain": cycle - current}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(get_light())

app.run(debug=True)