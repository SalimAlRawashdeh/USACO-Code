from RobotReplication.Cell import Cell
from RobotReplication.RobotGroup import RobotGroup

class Map:
    def __init__(self, mapLength, mapLayout):
        self.mapLength = mapLength
        self.mapLayout = mapLayout
        self.map = [[0 for i in range(int(mapLength))] for j in range(int(mapLength))]

    def runCalculations(self, numberOfSteps):
        numberOfStarts = self.createMap()
        self.initializeRobots(numberOfStarts)

        flag = False
        while flag is False:
            flag = True
            for i in range(RobotGroup.groupLength):
                if RobotGroup.groupList[i].getActive() is True:
                    flag = False

            if flag is False:
                for i in range(numberOfSteps):
                    for j in range(RobotGroup.groupLength):
                        if RobotGroup.groupList[j].getActive() is True:
                            self.moveRobotGroup(RobotGroup.groupList[j])

                for i in range(RobotGroup.groupLength):
                    if RobotGroup.groupList[i].getActive() is True:
                        self.duplicateRobotGroup(RobotGroup.groupList[i])


        self.printMap()

    def createMap(self):
        count = 0
        for i in range(self.mapLength):
            for j in range(self.mapLength):
                self.map[i][j] = Cell(self.mapLayout[i][j])
                if self.mapLayout[i][j] == "S":
                    count += 1

        return count

    def printMap(self):
        count = 0
        for i in range(self.mapLength):
            for j in range(self.mapLength):
                if self.map[i][j].getHadRobot() == True:
                    print("X", end="")
                    count += 1
                else:
                    print(self.map[i][j].getType(), end="")
            print("")

        print(count)

    def initializeRobots(self, numberOfStarts):
        for k in range (numberOfStarts):
            for i in range(self.mapLength):
                for j in range(self.mapLength):
                    if self.map[i][j].getType() == "S" and self.map[i][j].getHadRobot() is False:
                        startingRobotGroup = RobotGroup()
                        startingRobotGroup.addRobot(i, j)
                        RobotGroup.groupList.append(startingRobotGroup)
                        RobotGroup.groupLength += 1
                        self.map[i][j].setHadRobot()
                        break
                else:
                    continue
                break

    def moveRobotGroup(self, robotGroup):
        directionMap = [[1,0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(directionMap)):
            flag = False
            for j in range(robotGroup.getLength()):
                if self.map[robotGroup.getRobotGroup()[j].getRow() + directionMap[i][0]][robotGroup.getRobotGroup()[j].getColumn()+ directionMap[i][1]].getType() == "#":
                    flag = True

            if flag is False:
                newRobotGroup = RobotGroup()
                for j in range(robotGroup.getLength()):
                    row = robotGroup.getRobotGroup()[j].getRow() + directionMap[i][0]
                    column = robotGroup.getRobotGroup()[j].getColumn()+ directionMap[i][1]
                    newRobotGroup.addRobot(row, column)
                    self.map[row][column].setHadRobot()

                RobotGroup.groupList.append(newRobotGroup)
                RobotGroup.groupLength += 1

        robotGroup.deactivateGroup()

    def duplicateRobotGroup(self, robotGroup):
        flag = False
        for i in range(robotGroup.getLength()):
            row = robotGroup.getRobotGroup()[i].getRow()
            column = robotGroup.getRobotGroup()[i].getColumn()
            adjacentPositions = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]

            for pos in adjacentPositions:
                i, j = pos
                if self.map[i][j].getType() == "#":
                    flag = True

        if flag is False:
            for i in range(robotGroup.getLength()):
                row = robotGroup.getRobotGroup()[i].getRow()
                column = robotGroup.getRobotGroup()[i].getColumn()
                adjacentPositions = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
                for pos in adjacentPositions:
                    i, j = pos
                    robotGroup.addRobot(i, j)
                    self.map[i][j].setHadRobot()
        elif flag is True:
            robotGroup.deactivateGroup()
