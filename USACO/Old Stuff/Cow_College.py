file = open("12.in", "r")
data = file.read().strip()
dataList = data.split(" ")
optimalTuition = [ int(x) for x in dataList ]
file.close()

max = 0
count = 0
i = 0

while len(optimalTuition) > 0:
    min = optimalTuition[0]

    for x in optimalTuition:
        if x < min:
            min = x


    if max < min * len(optimalTuition):
        max = min * len(optimalTuition)
        i = min
        count += 1

    while min in optimalTuition:
        for x in (optimalTuition):
            if x == min:
                optimalTuition.remove(x)
                break


print (max, i)