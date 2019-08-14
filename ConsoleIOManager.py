from Command import Command
from Square import Square
from Validation import isValidSelection, isValidDestination



def getSelection(data, side):
    """Queries user to select a piece"""

    while True:
        try:
            row = int(input("Select Row: "))
            column = int((input("Select Column: ")))
            selection = Square(row, column)
            if(isValidSelection(selection, data, side)):
                break
        except ValueError:
            print("Invalid Input.")

    return selection


def getDestination(selection, data, side):
    """Queries user where to put a selected piece
    
    a -1, -1 destination lets the user make a new selection"""

    while True:
        try:
            row = int(input("Destination Row: "))
            column = int((input("Destination Column: ")))
            destination = Square(row, column)
            if(isValidDestination(selection, destination, data, side)):
                break
        except ValueError:
            print("Invalid Input.")

    return destination

def getCommand(side, data):
    """Queries user to select a piece and where to place the piece"""

    if(side == "white"):
        print("White's turn:")
    else:
        print("Black's turn:")

    while True:
        selection = getSelection(data, side)
        destination = getDestination(selection, data, side)
        if(not isResetCode(destination)):
            break

    return Command(selection, destination)


def isResetCode(destination):
    if(destination.row == -1 and destination.column == -1):
        return True
    else:
        return False