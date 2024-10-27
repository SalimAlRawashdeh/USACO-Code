from TargetPractice.Point import Point
from TargetPractice.Bessie import Bessie

class Line:
    def __init__(self, lineLength):
        self.lineLength = lineLength
        self.line = []

    def createLine(self, targetLocations, positionShift, numberOfTargets):
        targetIndex = 0
        for i in range(self.lineLength):
            if targetIndex < numberOfTargets and i - positionShift == targetLocations[targetIndex]:
                self.line.append(Point(True, False))
                targetIndex += 1
            else:
                self.line.append(Point(False, False))


    def shootTargets (self, numberOfInstructions, bessieInstructions):
        mainBessie = Bessie(numberOfInstructions)
        for i in range(numberOfInstructions):
            if bessieInstructions[i] == "L":
                mainBessie.moveLeft()
            elif bessieInstructions[i] == "R":
                mainBessie.moveRight()
            else:
                self.line[mainBessie.getCurrentLocation()].setIsBroken(True)

    def getTargetsBroken (self):
        count = 0
        for i in range(self.lineLength):
            if self.line[i].getIsBroken() is True:
                count += 1

        return count

    def resetLine (self):
        for i in range(self.lineLength):
            self.line[i].setIsBroken(False)


