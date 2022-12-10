def totalPriority(filename):
    f = open(filename, 'r')

    priorityScore = 0

    for rucksack in f:
        compartmentSize = int(len(rucksack) / 2)
        compartment1 = rucksack[:compartmentSize]
        compartment2 = rucksack[compartmentSize:]

        for c in compartment1:
            if(c in compartment2):
                if(c.islower()):
                    priorityScore += ord(c) - ord('a') + 1
                else:
                    priorityScore += ord(c) - ord('A') + 27
                break

    print(f'The total priority is {priorityScore}')


totalPriority('input.txt')
