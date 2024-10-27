def selectionSort(array, array2, array3, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] > array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        (array2[ind], array2[min_index]) = (array2[min_index], array2[ind])
        (array3[ind], array3[min_index]) = (array3[min_index], array3[ind])


file = open("TestCase.in", "r")
numberOfIterations = int(file.readline())

for i in range(numberOfIterations):
    numberofDays = 0

    listLength = int(file.readline())
    initialHeightData = file.readline().strip("\n").strip(" ")
    initialHeight = initialHeightData.split(" ")
    initialHeight = [int(x) for x in initialHeight]

    dailyGrowData = file.readline().strip("\n").strip(" ")
    dailyGrow = dailyGrowData.split(" ")
    dailyGrow = [int(x) for x in dailyGrow]

    tallerPlantsData = file.readline().strip("\n").strip(" ")
    tallerPlants = tallerPlantsData.split(" ")
    tallerPlants = [int(x) for x in tallerPlants]

    if listLength == 1:
        print(0)
    else:
        selectionSort(tallerPlants, dailyGrow, initialHeight, listLength)

        flag = False
        for j in range(listLength - 1):
            if dailyGrow[j] > dailyGrow[j + 1]:
                flag = True
                numberofDays = -1
            elif dailyGrow[j] == dailyGrow[j + 1] and initialHeight[j] >= initialHeight[j + 1]:
                flag = True
                numberofDays = -1

        while flag is False:
            flag = True
            for j in range (listLength - 1):
                if initialHeight [j] >= initialHeight[j + 1]:
                    flag = False

            if flag is False:
                for k in range (listLength):
                    initialHeight[k] = initialHeight[k] + dailyGrow[k]
                numberofDays += 1

        print(numberofDays)