def placeCrates(containers, line):
    for i in range(len(containers)):
        box = line[4*i+1]

        if(box == ' '):
            continue
        else:
            containers[i].append(box)


def moveCrates(containers, line):
    if(line != '\n'):
        operation = line.split(' ')

        numBoxes = int(operation[1])
        stack1 = int(operation[3]) - 1
        stack2 = int(operation[5]) - 1

        for i in range(numBoxes):
            box = containers[stack1].pop(0)
            containers[stack2].insert(0, box)


def getTopBoxes(filename):
    f = open(filename, 'r')
    lines = f.readlines()

    numContainers = int((len(lines[0]) + 1) / 4)
    containers = [[] for i in range(numContainers)]
    placing = True

    for line in lines:
        if(placing and line[1] == '1'):
            placing = False
        elif(placing):
            placeCrates(containers, line)
        else:
            moveCrates(containers, line)

    topBoxes = ''
    for i in range(len(containers)):
        topBoxes += containers[i][0]

    print(f'The top boxes are {topBoxes}')


getTopBoxes('input.txt')
