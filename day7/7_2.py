def getTotalSize(needed, fileStructure):
    minSize = 70000001

    for key in fileStructure:
        if(key == 'size'):
            if(fileStructure[key] > needed and fileStructure[key] < minSize):
                minSize = fileStructure[key]
        else:
            minSize = min(minSize, getTotalSize(needed, fileStructure[key]))

    return minSize


def getFileSizes(filename):
    f = open(filename, 'r')

    currentPath = []
    fileStructure = {}

    for line in f:
        line = line.strip()
        data = line.split(' ')

        if(data[0] == '$'):
            if(data[1] == 'cd'):
                if(data[2] == '..'):
                    currentPath.pop()
                else:
                    currentLoc = fileStructure

                    for c in currentPath:
                        currentLoc = currentLoc[c]

                    currentLoc[data[2]] = {'size': 0}
                    currentPath.append(data[2])

        elif(data[0].isdigit()):
            currentLoc = fileStructure

            for c in currentPath:
                currentLoc = currentLoc[c]
                currentLoc['size'] += int(data[0])

    needed = 30000000 - (70000000 - fileStructure['/']['size'])
    freedSpace = getTotalSize(needed, fileStructure)

    print(f'The freed space is {freedSpace}')


getFileSizes('input.txt')
