from flask import Flask, jsonify
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
    
    def countPiece(self):
        whiteCount = 0
        blackCount = 0
        for row in self.board:
            for cell in row:
                if(cell == 1):
                    whiteCount += 1
                elif(cell == -1):
                    blackCount += 1
        return [whiteCount, blackCount]

class Player():
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

    def countFlipPieces(self, board, x, y, direX, direY):
        global xOpe, yOpe
        #opponent side value
        oppSide = self.side * -1
        i = 1
        count = 0
        while board.board[yOpe(direY, y, i)][xOpe(direX, x, i)] == oppSide:
            count += 1
            i += 1
        return count
    
    def getFlipList(board, x, y):
        global countFlipPieces
        flipList = []
        flipList.append = countFlipPieces(board, x, y, 0, 1)
        flipList.append = countFlipPieces(board, x, y, 1, 1)
        flipList.append = countFlipPieces(board, x, y, 1, 0)
        flipList.append = countFlipPieces(board, x, y, 1, -1)
        flipList.append = countFlipPieces(board, x, y, 0, -1)
        flipList.append = countFlipPieces(board, x, y, -1, -1)
        flipList.append = countFlipPieces(board, x, y, -1, 0)
        flipList.append = countFlipPieces(board, x, y, -1, 1)
        return flipList

    #Check if the target. The target has to be empty and has at least 1 piece to be flipped
    def targetValidation(board, x, y):
        global getFlipList
        if(board.board[y][x] == 0 and (0 not in getFlipList(board, x, y))):
            return True
        else:
            return False
    
    def placePiece(self, board, x, y):
        global targetValidation
        if(targetValidation(board, x, y)):
            board.board[y][y] = self.side

    def flip(self, board, x, y):
        global getFlipList
        if getFlipList(board, x, y)[0] != 0:
            #flip up direction
            i = 1
            while board.board[y + i][x] == self.side * -1:
                board.board[y+i][x] *= -1
                i += 1
            #flip up right direction
            i = 1
            while board.board[y + i][x + i] == self.side * -1:
                board.board[y+i][x + i] *= -1
                i += 1
            #flip right direction
            i = 1
            while board.board[y][x + i] == self.side * -1:
                board.board[y][x + i] *= -1
                i += 1
            #flip down right direction
            i = 1
            while board.board[y - i][x + i] == self.side * -1:
                board.board[y+i][x + i] *= -1
                i += 1
            #flip down direction
            i = 1
            while board.board[y - i][x] == self.side * -1:
                board.board[y - i][x] *= -1
                i += 1
            #flip down left direction
            i = 1
            while board.board[y - i][x - i] == self.side * -1:
                board.board[y+i][x + i] *= -1
                i += 1
            #flip left direction
            i = 1
            while board.board[y][x - i] == self.side * -1:
                board.board[y][x - i] *= -1
                i += 1
            #flip up left direction
            i = 1
            while board.board[y + i][x - i] == self.side * -1:
                board.board[y +i ][x - i] *= -1
                i += 1
    
    def countValidCell(board):
        global targetValidation
        validCellCount = 0
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if targetValidation(board, j, i):
                    validCellCount += 1
        return validCellCount
    



@app.route("/", methods=['GET'])
def main():
    return '-1'

if __name__ == "__main__":
    app.run(debug=True, port=8080)