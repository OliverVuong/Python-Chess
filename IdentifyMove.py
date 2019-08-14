def indentifyMove(command, data):
    if (isEnPassant(command, data)):
        return "enPassant"
    elif (isCastling(command, data)):
        return "castling"
    else:
        return "regular"


def isEnPassant(command, data):
    if(data.getPiece(command.selection).pieceType == "pawn" and \
        command.selection.column != command.destination.column and \
        data.isEmpty(command.destination.row, command.destination.column)):
        return True
    else:
        return False


def isCastling(command, data):
    if(data.getPiece(command.selection).pieceType == "king" and \
        command.selection.column == 4 and \
        (command.destination.column == 0 or command.destination.column == 7)):
        return True
    else:
        return False
