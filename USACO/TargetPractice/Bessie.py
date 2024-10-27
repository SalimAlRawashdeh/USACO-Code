class Bessie:
    def __init__(self, currentLocation):
        self.currentLocation = currentLocation

    def moveLeft (self):
        self.currentLocation -= 1

    def moveRight (self):
        self.currentLocation += 1

    def getCurrentLocation(self):
        return self.currentLocation

