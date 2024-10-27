from itertools import chain, count

file = open("TestCase.in.in", "r")
currentChar = file.read(1)
chainLength = ""
while currentChar != " ":
    chainLength = chainLength + currentChar
    currentChar = file.read(1)

chainLength = int(chainLength)

numberOfIterations = int(file.readline())

animalDirections = []
maximumBucketCapacity = []
currentBuckectCapacity = []

for i in range(chainLength):
    animalDirections.append(file.read(1))

file.read(1)

data = file.readline()
maximumBucketCapacity = data.split(" ")
maximumBucketCapacity = [ int(x) for x in maximumBucketCapacity ]

maximumCapacity = 0

for i in range(chainLength):
    currentBuckectCapacity.append(maximumBucketCapacity[i])
    maximumCapacity = maximumCapacity + maximumBucketCapacity[i]

LitersLost = 0

for i in range(numberOfIterations):
    for j in range(chainLength):
            if currentBuckectCapacity[j] > 0:
                if animalDirections[j] == "L":
                    if j == 0:
                        currentBuckectCapacity[chainLength - 1] += 1
                        currentBuckectCapacity[j] -= 1

                    else:
                        currentBuckectCapacity[j - 1] += 1
                        currentBuckectCapacity[j] -= 1

                if animalDirections[j] == "R":
                    if j == chainLength - 1:
                        currentBuckectCapacity[0] += 1
                        currentBuckectCapacity[j] -= 1

                    else:
                        currentBuckectCapacity[j + 1] += 1
                        currentBuckectCapacity[j] -= 1


    for j in range(chainLength):
            if currentBuckectCapacity[j] > maximumBucketCapacity[j]:
                LitersLost += 1
                currentBuckectCapacity[j] = maximumBucketCapacity[j]
                print(maximumCapacity - LitersLost)


print(maximumCapacity - LitersLost)
