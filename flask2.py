# Flask Server
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Success"   

@app.route("/pathtest")
def index():
    return "Testing Path - completed"   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5003", debug=True)
