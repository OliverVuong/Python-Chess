from MovesSets.SharedFunctions import specific
from Square import Square


def getKnightMoves(startSquare, data):
    mySet = set()

    #up left
    specific(startSquare, Square(startSquare.row - 2, startSquare.column - 1),
             data, mySet)
    specific(startSquare, Square(startSquare.row - 1, startSquare.column - 2),
             data, mySet)

    #up right
    specific(startSquare, Square(startSquare.row - 2, startSquare.column + 1),
             data, mySet)
    specific(startSquare, Square(startSquare.row - 1, startSquare.column + 2),
             data, mySet)

    #down right
    specific(startSquare, Square(startSquare.row + 2, startSquare.column + 1),
             data, mySet)
    specific(startSquare, Square(startSquare.row + 1, startSquare.column + 2),
             data, mySet)

    #down left
    specific(startSquare, Square(startSquare.row + 2, startSquare.column - 1),
             data, mySet)
    specific(startSquare, Square(startSquare.row + 1, startSquare.column - 2),
             data, mySet)

    return mySet
