from CheckChecker import isInCheck
from HypotheticalScenario import HypotheticalScenario
from Command import Command

def isCheckmate(side, data):

    if not isInCheck(side, data):
        return False
    if canEscape(side, data):
        return False
    if canBeBlocked(side, data):
        return False


def canEscape(side, data):

    if side == "white":
        king = data.getWhiteKing()
    elif side == "black":
        king = data.getBlackKing()

    possibleEscapeMoves = king.getMovesSet(data) 

    for movesIt in possibleEscapeMoves:
        hypothetical = HypotheticalScenario(Command(king.location, movesIt), data)
        if not isInCheck(side, hypothetical):
            return True

    return False


def canBeBlocked(side, data):

    if side == "white":
        pieces = data.pieceLocations.whitePieces()
    elif side == "black":
        pieces = data.pieceLocations.blackPieces()

    for pieceIt in pieces:

        possibleEscapeMoves = pieceIt.getMovesSet(data) 

        for movesIt in possibleEscapeMoves:
            hypothetical = HypotheticalScenario(Command(pieceIt.location, movesIt), data)
            if not isInCheck(side, hypothetical):
                return True

    return False