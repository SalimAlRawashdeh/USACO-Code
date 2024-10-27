class Customer:
    def __init__(self, numberOfCookies, numberOfMuffins, time):
        self.numberOfCookies = numberOfCookies
        self.numberOfMuffins = numberOfMuffins
        self.time = time

    def getNumberOfCookies(self):
        return self.numberOfCookies

    def getNumberOfMuffins(self):
        return self.numberOfMuffins

    def getTime(self):
        return self.time
