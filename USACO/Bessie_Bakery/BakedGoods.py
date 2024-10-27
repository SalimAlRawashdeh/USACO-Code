class BakedGoods:
    def __init__(self, type, time):
        self.type = type
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time