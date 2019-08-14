from HypotheticalScenario import HypotheticalScenario
from Command import Command
from CheckChecker import isInCheck

def isInbounds(row, column):
    return row >= 0 and row < 8 and \
            column >= 0 and column < 8

def isOutOfBounds(square):
    if (square.row < 0 or square.row > 7 or \
        square.column < 0 or square.column > 7):
        print("Out of bounds.")
        return True
    else:
        return False


def noPieceSelected(square, data):
    if (data.isEmpty(square.row, square.column)):
        print("No Piece Selected.")
        return True
    else:
        return False


def wrongSideSelected(square, data, side):
    if (data.getSide(square.row, square.column) != side):
        print("Wrong side selected")
        return True
    else:
        return False


def isRedoSelectionCommand(square):
    if (square.row == -1 and square.column == -1):
        print("Redo Selection.")
        return True
    else:
        return False


def sameSquare(selection, destination):
    if (selection == destination):
        print("Destination must be different than selection")
        return True
    else:
        return False


def pieceIncapable(selection, destination, data):

    myPiece = data.getPiece(selection)
    myMovesSet = myPiece.getMovesSet(data)

    if (destination in myMovesSet):
        return False #piece is capable
    else:
        print("Piece Incapable")
        return True


def exposesKing(selection, destination, data, side):
    hypothetical = HypotheticalScenario(Command(selection, destination), data)
    return isInCheck(side, data)


def isValidSelection(square, data, side):
    if (isOutOfBounds(square)):
        return False
    if (noPieceSelected(square, data)):
        return False
    if (wrongSideSelected(square, data, side)):
        return False
    return True


def isValidDestination(selection, destination, data, side):
    """-1, -1 is a valid destination as it indicates the user wishes to \
    make a new selectin"""
    
    if (isRedoSelectionCommand(destination)):
        return True

    if (isOutOfBounds(destination)):
        return False
    if (sameSquare(selection, destination)):
        return False
    if (pieceIncapable(selection, destination, data)):
        return False
    if (exposesKing(selection, destination, data, side)):
        return False
    
    return True
