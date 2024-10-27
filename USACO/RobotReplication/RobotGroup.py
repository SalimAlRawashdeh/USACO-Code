from RobotReplication.Robot import Robot

class RobotGroup:
    groupList = []
    groupLength = 0

    def __init__(self):
        self.robotGroup = []
        self.isActive = True

    def getRobotGroup(self):
        return self.robotGroup

    def getLength(self):
        return len(self.robotGroup)

    def addRobot(self, row, column):
        self.robotGroup.append(Robot(row, column))

    def deactivateGroup(self):
        self.isActive = False

    def getActive(self):
        return self.isActive

