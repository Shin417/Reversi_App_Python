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

def countPiece():
    whiteCount = 0
    blackCount = 0
    for i in board:
        for j in board[i]:
            if(board[i][j] == 1):
                whiteCount += 1
            elif(board[i][j] == -1):
                blackCount += 1
    return [whiteCount, blackCount]




@app.route("/", method=['GET', 'POST'])
def main():




    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)