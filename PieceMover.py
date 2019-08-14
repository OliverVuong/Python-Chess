from IdentifyMove import indentifyMove
from HistoryRecorder import recordHistory
from Square import Square


def executeMove(command, data):

    moveType = indentifyMove(command, data) 

    recordHistory(command, data) 

    if(moveType == "regular"):
        regularMove(command, data) 
    elif(moveType == "enPassant"):
        enPassantMove(command, data)
    else:
        castlingMove(command, data) 


def regularMove(command, data):

    endSquare = command.destination
    if(not data.isEmpty(endSquare.row, endSquare.column)):
        data.destroyPiece(endSquare)
    data.movePiece(command.selection, endSquare)


def enPassantMove(command, data):
    data.movePiece(command.selection, command.destination)
    data.destroyPiece(command.selection.row, command.destination.column)


def castlingMove(command, data):
    row = command.selection.row

    #queen side castle
    if command.selection.column == 0:
        kingsColumn = 2
        rooksColumn = kingsColumn + 1
        data.movePiece(command.selection, Square(row, kingsColumn)) #move king
        data.movePiece(Square(0, row), Square(row, rooksColumn))    #move rook

    #king side castle
    else:
        kingsColumn = 6
        rooksColumn = kingsColumn - 1
        data.movePiece(command.selection, Square(row, kingsColumn)) #move king
        data.movePiece(Square(0, row), Square(row, rooksColumn))    #move rook
