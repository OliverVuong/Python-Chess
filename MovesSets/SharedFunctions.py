from Validation import isInbounds
from Square import Square


def up(startSquare, data, mySet):
    """Adds all possible destinations in the vertical up direction to a set"""

    rowIt = startSquare.row - 1
    column = startSquare.column

    while (isInbounds(rowIt, column)):

        potentialDestination = Square(rowIt, column)

        if (data.isEmpty(rowIt, column)):
            mySet.add(potentialDestination)
            rowIt = rowIt - 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break


def down(startSquare, data, mySet):
    """Adds all possible destinations in the vertical down direction to a set"""

    rowIt = startSquare.row + 1
    column = startSquare.column

    while (isInbounds(rowIt, column)):

        potentialDestination = Square(rowIt, column)

        if (data.isEmpty(rowIt, column)):
            mySet.add(potentialDestination)
            rowIt = rowIt + 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break


def left(startSquare, data, mySet):
    """Adds all possible destinations in the horizontal left direction to a set"""

    row = startSquare.row
    columnIt = startSquare.column - 1

    while (isInbounds(row, columnIt)):

        potentialDestination = Square(row, columnIt)

        if (data.isEmpty(row, columnIt)):
            mySet.add(potentialDestination)
            columnIt = columnIt - 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break


def right(startSquare, data, mySet):
    """Adds all possible destinations in the horizontal right direction to a set"""

    row = startSquare.row
    columnIt = startSquare.column + 1

    while (isInbounds(row, columnIt)):

        potentialDestination = Square(row, columnIt)

        if (data.isEmpty(row, columnIt)):
            mySet.add(potentialDestination)
            columnIt = columnIt + 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break


def upRight(startSquare, data, mySet):
    """Adds all possible destinations in the diagonal up right direction to a set"""

    rowIt = startSquare.row - 1
    columnIt = startSquare.column + 1

    while (isInbounds(rowIt, columnIt)):

        potentialDestination = Square(rowIt, columnIt)

        if (data.isEmpty(rowIt, columnIt)):
            mySet.add(potentialDestination)
            rowIt = rowIt - 1
            columnIt = columnIt + 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break

def upLeft(startSquare, data, mySet):
    """Adds all possible destinations in the diagonal up left direction to a set"""

    rowIt = startSquare.row - 1
    columnIt = startSquare.column - 1

    while (isInbounds(rowIt, columnIt)):

        potentialDestination = Square(rowIt, columnIt)

        if (data.isEmpty(rowIt, columnIt)):
            mySet.add(potentialDestination)
            rowIt = rowIt - 1
            columnIt = columnIt - 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break
            

def downRight(startSquare, data, mySet):
    """Adds all possible destinations in the diagonal down right direction to a set"""

    rowIt = startSquare.row + 1
    columnIt = startSquare.column + 1

    while (isInbounds(rowIt, columnIt)):

        potentialDestination = Square(rowIt, columnIt)

        if (data.isEmpty(rowIt, columnIt)):
            mySet.add(potentialDestination)
            rowIt = rowIt + 1
            columnIt = columnIt + 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break
            

def downLeft(startSquare, data, mySet):
    """Adds all possible destinations in the diagonal down left direction to a set"""

    rowIt = startSquare.row + 1
    columnIt = startSquare.column - 1

    while (isInbounds(rowIt, columnIt)):

        potentialDestination = Square(rowIt, columnIt)

        if (data.isEmpty(rowIt, columnIt)):
            mySet.add(potentialDestination)
            rowIt = rowIt + 1
            columnIt = columnIt - 1
        else:
            if (data.isDifferentSides(startSquare, potentialDestination)):
                mySet.add(potentialDestination)
            break


def specific(startSquare, endSquare, data, mySet):
    """Checks if a generic piece can move from a specific square to another"""

    if(isOutOfBounds(startSquare) or isOutOfBounds(endSquare)):
        return

    if (data.isEmpty(endSquare.row, endSquare.column) or \
        data.isDifferentSides(startSquare, endSquare)):
        mySet.add(endSquare)


def isOutOfBounds(square):
    if (square.row < 0 or square.row > 7 or \
        square.column < 0 or square.column > 7):
        return True
    else:
        return False