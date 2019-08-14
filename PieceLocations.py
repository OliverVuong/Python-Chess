from Piece import Piece


class PieceLocations:
    def __init__(self, testBoard=None):
        """Creates standard starting position or custom position"""
        if (testBoard == None):
            self.blackPieces = self.getStartingBlackPieces()
            self.whitePieces = self.getStartingWhitePieces()
            self.blackKing = Piece("black", "king", 0, 4) #direct access to kings for
            self.whiteKing = Piece("black", "king", 7, 4) #checkmate checks


        else:
            self.blackPieces = self.makeCustonBlackPieces(testBoard)
            self.whitePieces = self.makeCustonWhitePieces(testBoard)

    def getStartingBlackPieces(self):
        return {  # black queen, bishops, etc., no king
            Piece("black", "rook", 0, 0),
            Piece("black", "knight", 0, 1),
            Piece("black", "bishop", 0, 2),
            Piece("black", "queen", 0, 3),
            Piece("black", "king", 0, 4),
            Piece("black", "bishop", 0, 5),
            Piece("black", "knight", 0, 6),
            Piece("black", "rook", 0, 7),

            #black pawns
            Piece("black", "pawn", 1, 0),
            Piece("black", "pawn", 1, 1),
            Piece("black", "pawn", 1, 2),
            Piece("black", "pawn", 1, 3),
            Piece("black", "pawn", 1, 4),
            Piece("black", "pawn", 1, 5),
            Piece("black", "pawn", 1, 6),
            Piece("black", "pawn", 1, 7)
        }

    def getStartingWhitePieces(self):
        return {  # white queens, bishop, etc., no king
            Piece("white", "rook", 7, 0),
            Piece("white", "knight", 7, 1),
            Piece("white", "bishop", 7, 2),
            Piece("white", "queen", 7, 3),
            Piece("white", "king", 7, 4),
            Piece("white", "bishop", 7, 5),
            Piece("white", "knight", 7, 6),
            Piece("white", "rook", 7, 7),

            #white pawns
            Piece("white", "pawn", 6, 0),
            Piece("white", "pawn", 6, 1),
            Piece("white", "pawn", 6, 2),
            Piece("white", "pawn", 6, 3),
            Piece("white", "pawn", 6, 4),
            Piece("white", "pawn", 6, 5),
            Piece("white", "pawn", 6, 6),
            Piece("white", "pawn", 6, 7)
        }

    def makeCustonBlackPieces(self, testBoard):
        pass  #implement later

    def makeCustonWhitePieces(self, testBoard):
        pass  #implement later

    def getShallowCopy(self):
        
        shallowCopy = PieceLocations()

        shallowCopy.blackKing = Piece("black", "king", self.blackKing.row, self.blackKing.column)
        shallowCopy.whiteKing = Piece("black", "king", self.whiteKing.row, self.whiteKing.column)

        shallowCopy.blackPieces.clear()
        for pieceIt in self.blackPieces:
            shallowCopy.blackPieces.add(Piece(pieceIt.side, pieceIt.pieceType, pieceIt.row, pieceIt.column))

        shallowCopy.whitePieces.clear()
        for pieceIt in self.whitePieces:
            shallowCopy.blackPieces.add(Piece(pieceIt.side, pieceIt.pieceType, pieceIt.row, pieceIt.column))

        return shallowCopy