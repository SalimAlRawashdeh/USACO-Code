from RobotReplication.Map import Map

file = open("TestCase.in", "r")
mapLength, numberOfSteps = map(int, file.readline().split())
mapLayout = [[0 for i in range(int(mapLength))] for j in range(int(mapLength))]

for i in range(mapLength):
    for j in range(mapLength):
        currentChar = file.read(1)

        if currentChar == '\n':
            currentChar = file.read(1)

        mapLayout[i][j] = currentChar

mainMap = Map(mapLength, mapLayout)
mainMap.runCalculations(numberOfSteps)
