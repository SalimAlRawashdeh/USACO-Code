class Target:
    def __init__(target, neededPower):
        target.neededPower = neededPower
        target.isBroken = False
        target.type = "target"

    def getNeededPower(target):
        return target.neededPower

    def setIsBroken(target):
        target.isBroken = True

    def getIsBroken(target):
        return target.isBroken

    def getType(target):
        return target.type
