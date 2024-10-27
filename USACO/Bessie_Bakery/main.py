from Bessie_Bakery.Customer import Customer

file = open("TestCase.in", "r")
numberOfIterations = int(file.readline())

for i in range(numberOfIterations):
    file.readline()
    firstLine = file.readline().strip()
    numberOfCustomers, timeCookies, timeMuffins = map(int, firstLine.split())
    count = 0

    customers = []

    for i in range(numberOfCustomers):
        currentLine = file.readline().strip()
        numberOfCookies, numberOfMuffins, timeWaited = map(int, currentLine.split())
        customers.append(Customer(numberOfCookies, numberOfMuffins, timeWaited))

    for i in range(numberOfCustomers):
        flag = False
        while flag is False:
            if customers[i].getTime() < (customers[i].getNumberOfCookies() * timeCookies + customers[i].getNumberOfMuffins() * timeMuffins):
                cookiesLost = customers[i].getNumberOfCookies() * timeCookies - (customers[i].getNumberOfCookies() * (timeCookies - 1))
                muffinsLost = customers[i].getNumberOfMuffins() * timeMuffins - (customers[i].getNumberOfMuffins() * (timeMuffins - 1))

                if cookiesLost >= muffinsLost and timeCookies > 1:
                    timeCookies -= 1
                    count += 1
                    print(count)

                elif timeMuffins > 1:
                    timeMuffins -= 1
                    count += 1
                    print(count)

            else:
                flag = True

    print(count)

