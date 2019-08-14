class History:
    def __init__(self):
        self.whiteKingMoved = False
        self.blackKingMoved = False
        self.whiteLeftRookMoved = False
        self.whiteRightRookMoved = False
        self.blackLeftRookMoved = False
        self.blackRightRookMoved = False
        self.doubleMovedPawn = 0

    def getShallowCopy(self):

        shallowCopy = History()
        
        shallowCopy.whiteKingMoved = self.whiteKingMoved
        shallowCopy.blackKingMoved = self.blackKingMoved
        shallowCopy.whiteLeftRookMoved = self.whiteLeftRookMoved
        shallowCopy.whiteRightRookMoved = self.whiteRightRookMoved
        shallowCopy.blackLeftRookMoved = self.blackLeftRookMoved
        shallowCopy.blackRightRookMoved = self.blackRightRookMoved
        shallowCopy.doubleMovedPawn = self.doubleMovedPawn

        return shallowCopy