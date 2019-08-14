from Square import Square
from Validation import isOutOfBounds, isInbounds


def getPawnBlackMoves(startSquare, data):
    mySet = set()

    oneDown(startSquare, data, mySet);
    leftStrike(startSquare, data, mySet);
    rightStrike(startSquare, data, mySet);
    firstMoveDouble(startSquare, data, mySet);
    enPassant(startSquare, data, mySet);

    return mySet


def oneDown(startSquare, data, mySet):
    
    if(isOutOfBounds(startSquare)):
        return
    if(data.isEmpty(startSquare.row + 1, startSquare.column)):
        mySet.add(Square(startSquare.row + 1, startSquare.column))

    
def leftStrike(startSquare, data, mySet):
        
    endSquare = Square(startSquare.row + 1, startSquare.column - 1)
    
    if(isInbounds(endSquare.row, endSquare.column) and \
        data.isDifferentSides(startSquare, endSquare)):
        mySet.add(endSquare)

    
def rightStrike(startSquare, data, mySet):
        
    endSquare = Square(startSquare.row + 1, startSquare.column + 1)
    
    if(isInbounds(endSquare.row, endSquare.column) and \
        data.isDifferentSides(startSquare, endSquare)):
        mySet.add(endSquare)

    
def firstMoveDouble(startSquare, data, mySet):
    
    if(startSquare.row != 1):
        return
    if(not data.isEmpty(2, startSquare.column)):
        return
    if(not data.isEmpty(3, startSquare.column)):
        return
    
    mySet.add(Square(3, startSquare.column))
    

def enPassant(startSquare, data, mySet):
    pass