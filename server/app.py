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

    """
    Count how many pieces to be flipped next to the target place. Parameters(boardObject, targetX, targetY, checkDirectionX, checkDirectionY)
    direX = 0 & direY = 1  ==> check up direction of the target
    direX = 1 & direY = 1  ==> check up right direction of the target
    direX = 1 & direY = 0  ==> check left direction of the target
    direX = 1 & direY = -1  ==> check down right direction of the target
    direX = 0 & direY = -1  ==> check down direction of the target
    direX = -1 & direY = -1  ==> check down left direction of the target
    direX = -1 & direY = 0  ==> check left direction of the target
    direX = -1 & direY = 1  ==> check up left direction of the target
    """
    def xOpe(direX, a, b):
        if(direX == 1):
            return a + b
        elif(direX == -1):
            return a - b
        
    def yOpe(direY, a, b):
        if(direY == 1):
            return a + b
        elif(direY == -1):
            return a - b

    def countFlipPieces(board, x, y, direX, direY):
        global side
        #opponent side value
        oppSide = side * -1
        #check up direction
        





@app.route("/", method=['GET', 'POST'])
def main():




    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)