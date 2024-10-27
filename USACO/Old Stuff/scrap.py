file = open("copy.in", "r")
iterateLoop = file.readline()

for count in range(int(iterateLoop)):
    skipLine = file.readline()
    if count > 0:
        skipLine = file.readline()

    canvasLength = file.readline()
    canvasLength = int(canvasLength)
    canvasArr = [[0 for i in range(int(canvasLength))] for j in range(int(canvasLength))]
    testArr = [["." for i in range(int(canvasLength))] for j in range(int(canvasLength))]
    for i in range(canvasLength):
        for j in range(canvasLength):
            currentChar = file.read(1)

            if currentChar == '\n':
                currentChar = file.read(1)

            canvasArr[i][j] = currentChar

    file.read(1)

    stampLength = file.readline()
    stampLength = int(stampLength)
    stampArr = [[0 for i in range(stampLength)] for j in range(stampLength)]

    for i in range(stampLength):
        for j in range(stampLength):
            currentChar = file.read(1)

            if currentChar == '\n':
                currentChar = file.read(1)

            stampArr[i][j] = currentChar

    flag1 = "false"
    numberOfRotations = 0
    while flag1 == "false":
        flag2 = "false"

        for i in range(canvasLength + 1 - stampLength):
            for j in range(canvasLength + 1 - stampLength):
                flag2 = "false"
                for k in range(stampLength):
                    for l in range(stampLength):
                        if stampArr[k][l] == '*':
                            if canvasArr[i + k][j + l] == '.':
                                flag2 = "true"
                if flag2 == "false":
                    for k in range(stampLength):
                        for l in range(stampLength):
                            if stampArr[k][l] == '*':
                                testArr[i + k][j + l] = "*"

        if testArr == canvasArr:
            flag1 = "true"
            print("Yes")
        if numberOfRotations == 3:
            flag1 = "true"
            print("No")
            print(testArr)
        else:
            numberOfRotations += 1
            rotateArray(stampArr)
            print("newLine")