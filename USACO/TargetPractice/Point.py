class Point:
    def __init__(self, isTarget, isBroken):
        self.isTarget = isTarget
        self.isBroken = isBroken

    def getIsTarget(self):
        return self.isTarget

    def setIsBroken(self, isBroken):
        if self.isTarget is True:
            self.isBroken = isBroken

    def getIsBroken(self):
        return self.isBroken