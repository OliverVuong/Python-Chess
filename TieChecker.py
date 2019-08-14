def isTie(side, data):

    if side == "white":
        pieces = data.pieceLocations.whitePieces()
        pieces.add(data.getWhiteKing())
    elif side == "black":
        pieces = data.pieceLocations.blackPieces()
        pieces.add(data.getBlackKing())

    for pieceIt in pieces:

        allMoves = pieceIt.getMovesSet(data) 
        if len(allMoves) > 0:
            return False

    return True