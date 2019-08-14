class Command:
    """Consists of a selected square and a destination square"""

    def __init__(self, selection, destination):
        self.selection = selection
        self.destination = destination