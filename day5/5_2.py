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

        boxes = containers[stack1][0:numBoxes]
        containers[stack2] = boxes + containers[stack2]
        containers[stack1] = containers[stack1][numBoxes:]


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
