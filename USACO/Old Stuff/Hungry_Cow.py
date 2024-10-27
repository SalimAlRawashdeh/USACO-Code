# import itertools
# from pprint import pprint

file = open("13.in", "r")
fileContent = file.read().strip(" ")
fileContent = fileContent.replace("\n", " ")
fileContent = fileContent.split(" ")

fullList = [int(x) for x in fileContent]

fullList.pop(0)
Time = fullList.pop(0)
numberOfHaybales = 0
daysEaten = 0

for x in range(Time):
    if len(fullList) > 0:
        if fullList[0] == x + 1:
            fullList.pop(0)
            numberOfHaybales = numberOfHaybales + fullList.pop(0)
    else:
        daysEaten = daysEaten + numberOfHaybales
        break

    if numberOfHaybales != 0:
        daysEaten += 1
        print(x)
        numberOfHaybales -= 1

print(daysEaten)
