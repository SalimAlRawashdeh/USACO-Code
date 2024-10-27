from BessieCannonball.JumpPad import JumpPad
from BessieCannonball.Target import Target


class Line:
    def __init__(line, lineLength, ballIndex):
        line.lineLength = lineLength
        line.list = []
        line.ballIndex = ballIndex
        line.numberOfBrokenTargets = 0
        line.lastVisitedJumpPad = "null"

    def addToList (line, type, attribute):
        if type == "1":
            line.list.append(Target(attribute))
        else:
            line.list.append(JumpPad(attribute))

    def isBallInLine (line):
        if 0 <= line.ballIndex <= line.lineLength:
            return True
        else:
            return False

    def getNumberOfBrokenTargets (line):
        return line.numberOfBrokenTargets

    def moveBall (line, ball):
        if line.list[line.ballIndex].getType() == "target":
            if abs(ball.getVelocity()) >= line.list[line.ballIndex].getNeededPower():
                if line.list[line.ballIndex].getIsBroken() is False:
                    line.numberOfBrokenTargets += 1
                    line.list[line.ballIndex].setIsBroken()

        else:
            if line.lastVisitedJumpPad == "null":
                line.lastVisitedJumpPad = line.list[line.ballIndex]
            elif line.lastVisitedJumpPad.getPower() == 0 and line.list[line.ballIndex].getPower() == 0:
                return "break"


            if ball.getVelocity() < 0:
                ball.setVelocity(abs(ball.getVelocity()) + line.list[line.ballIndex].getPower())
            else:
                ball.setVelocity(-(ball.getVelocity() + line.list[line.ballIndex].getPower()))


        line.ballIndex += ball.getVelocity()




