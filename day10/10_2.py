def updateCycle(cycleNumber, output, x):
    if(cycleNumber >= x - 1 and cycleNumber <= x + 1):
        output[-1] += '#'
    else:
        output[-1] += '.'

    cycleNumber += 1

    if(cycleNumber % 40 == 0):
        cycleNumber = 0
        print(output[-1])
        output.append('')

    return cycleNumber


def getSignalStrength(filename):
    f = open(filename, 'r')

    x = 1
    cycleNumber = 0
    output = ['']

    for line in f:
        command = line.split()[0]

        if(command == 'noop'):
            cycleNumber = updateCycle(cycleNumber, output, x)

        elif(command == 'addx'):
            numToAdd = int(line.split()[1])

            cycleNumber = updateCycle(cycleNumber, output, x)
            cycleNumber = updateCycle(cycleNumber, output, x)

            x += numToAdd


getSignalStrength('input.txt')
