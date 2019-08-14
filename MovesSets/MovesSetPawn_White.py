from Square import Square
from Validation import isOutOfBounds, isInbounds


def getPawnWhiteMoves(startSquare, data):
    mySet = set()
    
    oneUp(startSquare, data, mySet);
    leftStrike(startSquare, data, mySet);
    rightStrike(startSquare, data, mySet);
    firstMoveDouble(startSquare, data, mySet);
    enPassant(startSquare, data, mySet);
    
    return mySet


def oneUp(startSquare, data, mySet):

    if(isOutOfBounds(startSquare)):
        return
    if(data.isEmpty(startSquare.row - 1, startSquare.column)):
        mySet.add(Square(startSquare.row - 1, startSquare.column))

    
def leftStrike(startSquare, data, mySet):

    endSquare = Square(startSquare.row - 1, startSquare.column - 1)
    
    if(isInbounds(endSquare.row, endSquare.column) and \
        data.isDifferentSides(startSquare, endSquare)):
        mySet.add(endSquare)

    
def rightStrike(startSquare, data, mySet):
    
    endSquare = Square(startSquare.row - 1, startSquare.column + 1)
    if(isInbounds(endSquare.row, endSquare.column) and \
            data.isDifferentSides(startSquare, endSquare)):
        
        mySet.add(endSquare)

    
def firstMoveDouble(startSquare, data, mySet):
    
    if(startSquare.row != 6):
        return
    if(not data.isEmpty(4, startSquare.column)):
        return
    if(not data.isEmpty(5, startSquare.column)):
        return
    
    mySet.add(Square(4, startSquare.column))
    

def enPassant(startSquare, data, mySet):
    pass