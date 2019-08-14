from MovesSets.SharedFunctions import upRight, downRight, upLeft, downLeft, \
                                        up, right, down, left

                
def getQueenMoves(startSquare, data):
    mySet = set()

    up(startSquare, data, mySet)
    right(startSquare, data, mySet)
    left(startSquare, data, mySet)
    down(startSquare, data, mySet)
    
    upRight(startSquare, data, mySet)
    downRight(startSquare, data, mySet)
    upLeft(startSquare, data, mySet)
    downLeft(startSquare, data, mySet)
    
    return mySet