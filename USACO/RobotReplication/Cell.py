class Cell:
    def __init__(self, type):
        self.type = type
        self.hadRobot = False
        self.hasBeenCalled = False

    def getType(self):
        return self.type

    def setHadRobot(self):
        self.hadRobot = True

    def getHadRobot(self):
        return self.hadRobot

    def getHasBeenCalled(self):
        return self.hasBeenCalled

    def setHasBeenCalled(self):
        if self.type == "S":
            self.hasBeenCalled = True

