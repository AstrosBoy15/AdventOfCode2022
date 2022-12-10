def getTotalSize(fileStructure):
    total = 0

    for key in fileStructure:
        if(key == 'size'):
            if(fileStructure[key] < 100000):
                total += fileStructure[key]
        else:
            total += getTotalSize(fileStructure[key])

    return total


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

    totalSize = getTotalSize(fileStructure)

    print(f'The total size is {totalSize}')


getFileSizes('input.txt')
