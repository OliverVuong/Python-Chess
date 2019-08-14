# Prints the board to the console  

def printBoard(data):
    """Prints a chess board representation to console"""
    
    print("   0   1   2   3   4   5   6   7")
    for rowIndex, row in enumerate(data.board.board):
        for piece in row:
            if piece == 0:
                print('   0', end='')
            else:
                print('  ' + str(piece), end ='')
        print('   ' + str(rowIndex))