class Board:
    """2D array that maps location to pieces"""

    def __init__(self, pieceLocations=None):
        self.board = self.getEmptyBoard()
        for v in pieceLocations.blackPieces:
            self.board[v.location.row][v.location.column] = v
        for v in pieceLocations.whitePieces:
            self.board[v.location.row][v.location.column] = v

    def getEmptyBoard(self):
        return [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    def isEmpty(self, row, column):
        return self.board[row][column] == 0

    def isWhite(self, row, column):
        """Returns True if space is white, returns false if black or empty."""

        if (self.isEmpty(row, column)):
            return False
        elif (self.board[row][column].side == "white"):
            return True
        else:
            return False

    def isBlack(self, row, column):
        if (self.isEmpty(row, column)):
            return False
        elif (self.board[row][column].side == "black"):
            return True
        else:
            return False

    def getSide(self, row, column):
        if (self.isEmpty(row, column)):
            return ""
        else:
            return self.board[row][column].side

    def isDifferentSides(self, square1, square2):
        if (self.isEmpty(square1.row, square1.column)):
            return False
        if (self.isEmpty(square2.row, square2.column)):
            return False

        return self.getSide(square1.row, square1.column) != self.getSide(
            square2.row, square2.column)
