from Square import Square
from MovesSets.MovesSetBishop import getBishopMoves
from MovesSets.MovesSetKing import getKingMoves
from MovesSets.MovesSetKnight import getKnightMoves
from MovesSets.MovesSetPawn_Black import getPawnBlackMoves
from MovesSets.MovesSetPawn_White import getPawnWhiteMoves
from MovesSets.MovesSetQueen import getQueenMoves
from MovesSets.MovesSetRook import getRookMoves

class Piece:
    """Represents an individual chess piece"""

    def __init__(self, side, pieceType, row, column):
        self.side = side
        self.pieceType = pieceType
        self.location = Square(row, column)
        self.isAlive = True

    def move(self, row, column):
        self.location.row = row
        self.location.column = column

    def destroy(self):
        self.isAlive = False
        self.location.row = -1
        self.location.column = -1

    def __str__(self):
        if(self.side == "black"):
            sideMod = "-"
        else:
            sideMod = " "

        if(self.pieceType == "king"):
            return sideMod + "K"
        elif(self.pieceType == "queen"):
            return sideMod + "Q"
        elif(self.pieceType == "bishop"):
            return sideMod + "B"
        elif(self.pieceType == "knight"):
            return sideMod + "N"
        elif(self.pieceType == "rook"):
            return sideMod + "R"
        elif(self.pieceType == "pawn"):
            return sideMod + "P"
        else:
            return "0"

    def getMovesSet(self, data):
        if(self.pieceType == "king"):
            return getKingMoves(self.location, data)
        elif(self.pieceType == "queen"):
            return getQueenMoves(self.location, data)
        elif(self.pieceType == "bishop"):
            return getBishopMoves(self.location, data)
        elif(self.pieceType == "knight"):
            return getKnightMoves(self.location, data)
        elif(self.pieceType == "rook"):
            return getRookMoves(self.location, data)
        elif(self.pieceType == "pawn" and self.side == "black"):
            return getPawnBlackMoves(self.location, data)
        elif(self.pieceType == "pawn" and self.side == "white"):
            return getPawnWhiteMoves(self.location, data)
        else:
            print("Unknown Piece. Cannot retrieve movesSet")
            return set()