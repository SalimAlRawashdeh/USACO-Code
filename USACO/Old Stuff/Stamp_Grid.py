def rotateArray(arr):
    layerCount = 0
    while layerCount <= len(arr) - layerCount:
        j = layerCount
        while j < len(arr) - layerCount - 1:
            temp1 = arr[layerCount][len(arr) - j - 1]
            arr[layerCount][len(arr) - j - 1] = arr[j][layerCount]


            temp2 = arr[len(arr) - j - 1][len(arr) - layerCount - 1]
            arr[len(arr) - j - 1][len(arr) - layerCount - 1] = temp1

            temp1 = arr[len(arr) - layerCount - 1][j]
            arr[len(arr) - layerCount - 1][j] = temp2

            arr[j][layerCount] = temp1

            j += 1

        layerCount += 1


file = open("14.in", "r")
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
            break
        if numberOfRotations == 3:
            flag1 = "true"
            print("No")
            break

        else:
            numberOfRotations += 1
            rotateArray(stampArr)

