def getNumberOfOverlaps(filename):
    f = open(filename, 'r')

    numOverlaps = 0

    for pair in f:
        elves = pair.split(',')

        elf1 = elves[0].split('-')
        elf2 = elves[1].split('-')

        if(int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])):
            numOverlaps += 1
        elif(int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])):
            numOverlaps += 1

        elif(int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])):
            numOverlaps += 1
        elif(int(elf1[1]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
            numOverlaps += 1

    print(f'The number of overlaps are {numOverlaps}')


getNumberOfOverlaps('input.txt')
