class Square:
    """Represents a location on a chess board"""

    def __init__(self, row, column):
        self.row, self.column = row, column

    def __eq__(self, value):
        return self.row == value.row and self.column == value.column

    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"

    def __hash__(self):
        return (100 * self.row) + self.column

    def __repr__(self):
        return self.__str__()