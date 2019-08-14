from PieceLocations import PieceLocations
from Board import Board
from History import History


class Data:
    """Houses all the data for the chess game

    consists of 
    a 2D list that maps location to piece 
    a dictionary that maps pieceID to location
    historical data for en passant and castling"""

    def __init__(self, inputBoard=None):
        if (inputBoard == None):
            self.pieceLocations = PieceLocations()
            self.board = Board(self.pieceLocations)
            self.history = History()
        else:
            pass  #implement later

    def isEmpty(self, row, column):
        return self.board.isEmpty(row, column)

    def isWhite(self, row, column):
        return self.board.isWhite(row, column)

    def getSide(self, row, column):
        return self.board.getSide(row, column)

    def isDifferentSides(self, square1, square2):
        return self.board.isDifferentSides(square1, square2)

    def getPiece(self, square):
        return self.board.board[square.row][square.column]

    def destroyPiece(self, square):
        self.getPiece(square).destroy()
        self.board.board[square.row][square.column] = 0

    def movePiece(self, startSquare, endSquare):

        myPiece = self.getPiece(startSquare)
        myPiece.move(endSquare.row, endSquare.column)
        self.board.board[startSquare.row][startSquare.column] = 0
        self.board.board[endSquare.row][endSquare.column] = myPiece

    def getWhiteKing(self):
        return self.pieceLocations.whiteKing

    def getBlackKing(self):
        return self.pieceLocations.blackKing

    def getShallowPieceCopy(self):
        self.pieceLocations.getShallowCopy()

    def getShallowHistoryCopy(self):
        self.history.getShallowCopy()