from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*') 

@app.route("/")
def main():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)