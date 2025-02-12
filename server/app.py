from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')


board = [[2,2,2,2,2,2,2,2,2,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,1,-1,0,0,0,2],
         [2,0,0,0,-1,1,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,2,2,2,2,2,2,2,2,2]
         ]



@app.route("/")
def main():




    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)