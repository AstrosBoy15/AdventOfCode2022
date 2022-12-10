import math


def getNumberVisited(filename):
    f = open(filename, 'r')

    headPos = [0, 0]
    tailPos = [0, 0]
    tailVisited = set()
    tailVisited.add(tuple(tailPos))

    directions = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }

    for line in f:
        direction = line.split(' ')[0]
        movement = int(line.split(' ')[1])

        for i in range(movement):
            velocity = directions[direction]
            headPos[0] += velocity[0]
            headPos[1] += velocity[1]

            difference = [headPos[0] - tailPos[0], headPos[1] - tailPos[1]]
            squaredDistance = difference[0]**2 + difference[1]**2

            if(squaredDistance == 4 or squaredDistance == 8):
                difference[0] = int(difference[0]/2)
                difference[1] = int(difference[1]/2)
            elif(squaredDistance == 5):
                difference[0] = int(
                    difference[0] / abs(difference[0]) * math.ceil(abs(difference[0]/2.0)))
                difference[1] = int(
                    difference[1] / abs(difference[1]) * math.ceil(abs(difference[1]/2.0)))
            else:
                difference = [0, 0]

            tailPos[0] += difference[0]
            tailPos[1] += difference[1]

            tailVisited.add(tuple(tailPos))

    print(f'The number of squares visited is {len(tailVisited)}')


getNumberVisited('input.txt')
