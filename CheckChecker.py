from Validation import isInbounds

def isInCheck(side, data):
    if side =="white":
        return isWhiteKingInCheck(data)
    elif side == "black":
        return isBlackKingInCheck(data) 
    else:
        print("Error in CheckChecker.isInCheck -unkown side")

def isWhiteKingInCheck(data):
    whiteKing = data.getWhiteKing()

    if checkedByKnight(whiteKing.location, "white", data) :
        return True
    if checkedFromDown(whiteKing.location, "white", data):
        return True
    if checkedFromLeft(whiteKing.location, "white", data):
        return True
    if checkedFromRight(whiteKing.location, "white", data):
        return True


    if checkedFromUpLeft(whiteKing.location, "white", data):
        return True
    if checkedFromUpRight(whiteKing.location, "white", data):
        return True
    if checkedFromDownRight(whiteKing.location, "white", data):
        return True
    if checkedFromDownLeft(whiteKing.location, "white", data):
        return True
    return False

def isBlackKingInCheck(data):
    blackKing = data.getBlackKing()

    if checkedByKnight(blackKing.location, "black", data) :
        return True
    if checkedFromDown(blackKing.location, "black", data):
        return True
    if checkedFromLeft(blackKing.location, "black", data):
        return True
    if checkedFromRight(blackKing.location, "black", data):
        return True


    if checkedFromUpLeft(blackKing.location, "black", data):
        return True
    if checkedFromUpRight(blackKing.location, "black", data):
        return True
    if checkedFromDownRight(blackKing.location, "black", data):
        return True
    if checkedFromDownLeft(blackKing.location, "black", data):
        return True
    return False

def checkedByKnight(kingLocation, side, data):

    if knightAt(kingLocation.row - 1, kingLocation.column - 2, side, data):
        return True
    if knightAt(kingLocation.row - 2, kingLocation.column - 1, side, data):
        return True
    if knightAt(kingLocation.row - 2, kingLocation.column + 1, side, data):
        return True
    if knightAt(kingLocation.row - 1, kingLocation.column + 2, side, data):
        return True
    if knightAt(kingLocation.row + 1, kingLocation.column + 2, side, data):
        return True
    if knightAt(kingLocation.row + 2, kingLocation.column + 1, side, data):
        return True
    if knightAt(kingLocation.row + 2, kingLocation.column - 1, side, data):
        return True
    if knightAt(kingLocation.row + 1, kingLocation.column - 2, side, data):
        return True
    return False


def knightAt(row, column, side, data):
    if not isInbounds(row, column):
        return False
    if data.isEmpty(row, column):
        return False
    if data.getSide(row, column) == side:
        return False
    if data.getPiece(row, column).pieceType != "knight":
        return False
    
    return True


def checkedFromUp(kingLocation, side, data):

    rowIt = kingLocation.row - 1
    column = kingLocation.column

    while isInbounds(rowIt, column):
        iteratorPiece = data.getPiece(rowIt, column)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        rowIt = rowIt - 1

    return False

def checkedFromDown(kingLocation, side, data):

    rowIt = kingLocation.row + 1
    column = kingLocation.column

    while isInbounds(rowIt, column):
        iteratorPiece = data.getPiece(rowIt, column)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        rowIt = rowIt + 1

    return False


def checkedFromLeft(kingLocation, side, data):

    row = kingLocation.row - 1
    columnIt = kingLocation.column

    while isInbounds(row, columnIt):
        iteratorPiece = data.getPiece(row, columnIt)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        columnIt = columnIt - 1

    return False


def checkedFromRight(kingLocation, side, data):

    row = kingLocation.row + 1
    columnIt = kingLocation.column

    while isInbounds(row, columnIt):
        iteratorPiece = data.getPiece(row, columnIt)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        columnIt = columnIt + 1

    return False


def checkedFromUpLeft(kingLocation, side, data):

    rowIt = kingLocation.row - 1
    columnIt = kingLocation.column - 1

    while isInbounds(rowIt, columnIt):
        iteratorPiece = data.getPiece(rowIt, columnIt)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        rowIt = rowIt - 1
        columnIt = columnIt - 1

    return False


def checkedFromUpRight(kingLocation, side, data):

    rowIt = kingLocation.row - 1
    columnIt = kingLocation.column + 1

    while isInbounds(rowIt, columnIt):
        iteratorPiece = data.getPiece(rowIt, columnIt)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        rowIt = rowIt - 1
        columnIt = columnIt + 1

    return False


def checkedFromDownRight(kingLocation, side, data):

    rowIt = kingLocation.row + 1
    columnIt = kingLocation.column + 1

    while isInbounds(rowIt, columnIt):
        iteratorPiece = data.getPiece(rowIt, columnIt)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        rowIt = rowIt + 1
        columnIt = columnIt + 1

    return False


def checkedFromDownLeft(kingLocation, side, data):

    rowIt = kingLocation.row + 1
    columnIt = kingLocation.column - 1

    while isInbounds(rowIt, columnIt):
        iteratorPiece = data.getPiece(rowIt, columnIt)
        if(iteratorPiece == 0): #empty
            pass                #continue to look at next row
        elif(iteratorPiece.side == side):
            return False        #friendly unit found
        elif(iteratorPiece.pieceType == "rook" or \
             iteratorPiece.pieceType == "queen"):
             return True

        rowIt = rowIt + 1
        columnIt = columnIt - 1

    return False

