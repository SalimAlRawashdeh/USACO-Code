import sys
sys.set_int_max_str_digits(0)

file = open("13.in", "r")
iterateLoop = file.readline()
for count in range(int(iterateLoop)):
    currentInt = file.readline()
    currentInt = int(currentInt)

    if currentInt % 10 == 0:
        print("E")
    else:
        print("B")