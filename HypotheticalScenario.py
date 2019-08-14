from Board import Board
from PieceMover import executeMove

class HypotheticalScenario:

    def __innit__(self, command, data):
        self.pieceLocations = data.getShallowPieceCopy()
        self.board = Board(self.pieceLocations)
        self.history = data.getShallowHistoryCopy()
        executeMove(command, data)

