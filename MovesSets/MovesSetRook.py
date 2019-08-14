from MovesSets.SharedFunctions import up, right, down, left


def getRookMoves(startSquare, data, mySet):
    mySet = set()

    up(startSquare, data, mySet)
    right(startSquare, data, mySet)
    left(startSquare, data, mySet)
    down(startSquare, data, mySet)

    return mySet