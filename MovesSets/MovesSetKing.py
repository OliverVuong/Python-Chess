from MovesSets.SharedFunctions import specific
from Square import Square


def getKingMoves(startSquare, data):

    mySet = set()

    specific(startSquare, Square(startSquare.row - 1, startSquare.column - 1),
             data, mySet)  #up left
    specific(startSquare, Square(startSquare.row - 1, startSquare.column),
             data, mySet)  #up
    specific(startSquare, Square(startSquare.row - 1, startSquare.column + 1),
             data, mySet)  #up right

    specific(startSquare, Square(startSquare.row, startSquare.column + 1),
             data, mySet)  #right

    specific(startSquare, Square(startSquare.row + 1, startSquare.column + 1),
             data, mySet)  #down right
    specific(startSquare, Square(startSquare.row + 1, startSquare.column),
             data, mySet)  #down
    specific(startSquare, Square(startSquare.row + 1, startSquare.column - 1),
             data, mySet)  #down left

    specific(startSquare, Square(startSquare.row, startSquare.column - 1),
             data, mySet)  #left

    return mySet
