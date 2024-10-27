class Robot:

    robotList = []
    listLength = 0

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def moveRobot(self, direction):
        if direction == 'up':
            self.row -= 1
        elif direction == 'down':
            self.row += 1
        elif direction == 'left':
            self.column -= 1
        elif direction == 'right':
            self.column += 1

