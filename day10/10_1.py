def updateCycle(signalStrength, cycleNumber, x):
    cycleNumber += 1

    if((cycleNumber + 20) % 40 == 0):
        signalStrength += cycleNumber * x

    return signalStrength, cycleNumber


def getSignalStrength(filename):
    f = open(filename, 'r')

    x = 1
    cycleNumber = 0
    signalStrength = 0

    for line in f:
        command = line.split()[0]

        if(command == 'noop'):
            signalStrength, cycleNumber = updateCycle(
                signalStrength, cycleNumber, x)

        elif(command == 'addx'):
            numToAdd = int(line.split()[1])

            signalStrength, cycleNumber = updateCycle(
                signalStrength, cycleNumber, x)
            signalStrength, cycleNumber = updateCycle(
                signalStrength, cycleNumber, x)

            x += numToAdd

    print(f'The signal strength is {signalStrength}')


getSignalStrength('input.txt')
