file = open("TestCase.in", "r")
numberOfIterations = int(file.readline())

for i in range(numberOfIterations):
    numberOfCows = int(file.readline())
    data = file.readline()
    cowPreferences = data.split(" ")
    cowPreferences = [int(x) for x in cowPreferences]

    bestFlavors = []

    if len(cowPreferences) > 2:
        for j in range(numberOfCows - 2):
            if cowPreferences[j] == cowPreferences[j+1] or cowPreferences[j] == cowPreferences[j+2]:
                if len(bestFlavors) == 0:
                    bestFlavors.append(cowPreferences[j])
                else:
                    flag = "false"

                    for k in range(len(bestFlavors)):
                        if cowPreferences[j] == bestFlavors[k]:
                            flag = "true"

                    if flag == "false":
                         bestFlavors.append(cowPreferences[j])

    if len(cowPreferences) == 2:
        if cowPreferences[0] == cowPreferences[1]:
            bestFlavors.append(cowPreferences[0])

    if len(cowPreferences) == 1:
        bestFlavors.append(cowPreferences[0])

    bestFlavors.sort()

    if len(bestFlavors) == 0:
        print("-1")
    else:
        print(bestFlavors)

