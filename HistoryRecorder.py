def recordHistory(command, data):

    movedPiece = data.getPiece(command.selection)

    if movedPiece.pieceType == "pawn":
        if movedPiece.side == "white" and \
            command.selection.row == 6 and \
            command.destination.row == 4:
            pass
        elif movedPiece.side == "black" and \
             command.selection.row == 1 and \
             command.destination.row == 3:
             pass
    elif movedPiece.pieceType == "king":
        if movedPiece.side == "white":
            pass
        elif movedPiece.side == "black":
             pass
    elif movedPiece.pieceType == "rook":
        if movedPiece.side == "white":
            if command.selection.column == 0:
                pass
            elif command.selection.column == 7:
                 pass
        elif movedPiece.side == "black":
            if command.selection.column == 0:
                pass
            elif command.selection.column == 7:
                 pass