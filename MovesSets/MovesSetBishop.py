from MovesSets.SharedFunctions import upRight, downRight, upLeft, downLeft


def getBishopMoves(startSquare, data):

    mySet = set()
    upRight(startSquare, data, mySet)
    downRight(startSquare, data, mySet)
    upLeft(startSquare, data, mySet)
    downLeft(startSquare, data, mySet)

    return mySet