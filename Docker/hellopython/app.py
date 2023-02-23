import time
from flask import Flask

app = Flask(__name__)

START = time.time()

def elasped():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route("/")
def route():
    return "Hello All (up %s)\n" % elasped()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8070) 