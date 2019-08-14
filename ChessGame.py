from Data import Data
from Printer import printBoard
from ConsoleIOManager import getCommand
from PieceMover import executeMove
from CheckMateChecker import isCheckmate
from TieChecker import isTie


def getSide(turn):
    """White goes on odd turns, black goes on even turns"""
    
    if (turn % 2 == 1):
        return "white"
    else:
        return "black"


def runChessGame():
    """Begins and executes a game of chess to completion"""

    myData = Data()
    turn = 1
    printBoard(myData)

    while not isCheckmate( getSide(turn), myData ) and \
          not isTie( getSide(turn), myData ):
        command = getCommand(getSide(turn), myData)
        executeMove(command, myData)
        printBoard(myData)
        turn = turn + 1
