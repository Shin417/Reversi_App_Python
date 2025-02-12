from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

class Board():
    def __init__(self):
        self.board = [[2,2,2,2,2,2,2,2,2,2],
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
        global board
        whiteCount = 0
        blackCount = 0
        for i in board:
            for j in board[i]:
                if(board[i][j] == 1):
                    whiteCount += 1
                elif(board[i][j] == -1):
                    blackCount += 1
        return [whiteCount, blackCount]

class Player():
    validCellCount = 0
    def __init__(self, side):
        self.side = side

    






@app.route("/", method=['GET', 'POST'])
def main():




    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)