from TargetPractice.Line import Line

file = open("TestCase.in", "r")

currentChar = file.read(1)
numberOfTargets = ""
while currentChar != " ":
    numberOfTargets = numberOfTargets + currentChar
    currentChar = file.read(1)

numberOfTargets = int(numberOfTargets)

numberOfInstructions = int(file.readline())
lineLength = 2 * numberOfInstructions + 1

targetLocations = file.readline()
targetLocations = targetLocations.split(" ")
targetLocations = [ int(x) for x in targetLocations ]

bessieInstructions = file.readline()
bessieInstructions = [x for x in bessieInstructions]

targetLocations.sort()
mainLine = Line(lineLength)
mainLine.createLine(targetLocations, numberOfInstructions, numberOfTargets)
mainLine.shootTargets(numberOfInstructions, bessieInstructions)
maximumNumberBroken = mainLine.getTargetsBroken()

for i in range(numberOfInstructions):
    mainLine.resetLine()
    if bessieInstructions[i] == "R":
        for k in range(2):
            if k == 0:
                bessieInstructions[i] = "L"
            else:
                bessieInstructions[i] = "F"
            mainLine.shootTargets(numberOfInstructions, bessieInstructions)
            if mainLine.getTargetsBroken() > maximumNumberBroken:
                maximumNumberBroken = mainLine.getTargetsBroken()

            bessieInstructions[i] = "R"
            mainLine.resetLine()

    elif bessieInstructions[i] == "L":
        for k in range(2):
            if k == 0:
                bessieInstructions[i] = "R"
            else:
                bessieInstructions[i] = "F"
            mainLine.shootTargets(numberOfInstructions, bessieInstructions)
            if mainLine.getTargetsBroken() > maximumNumberBroken:
                maximumNumberBroken = mainLine.getTargetsBroken()

            bessieInstructions[i] = "L"
            mainLine.resetLine()

    else:
        for k in range(2):
            if k == 0:
                bessieInstructions[i] = "L"
            else:
                bessieInstructions[i] = "R"
            mainLine.shootTargets(numberOfInstructions, bessieInstructions)
            if mainLine.getTargetsBroken() > maximumNumberBroken:
                maximumNumberBroken = mainLine.getTargetsBroken()

            bessieInstructions[i] = ("F")
            mainLine.resetLine()

    print("hello")

print(maximumNumberBroken)
