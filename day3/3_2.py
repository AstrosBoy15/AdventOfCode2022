def totalPriority(filename):
    f = open(filename, 'r')

    priorityScore = 0

    for elf1 in f:
        elf2 = next(f)
        elf3 = next(f)

        for c in elf1:
            if(c in elf2 and c in elf3):
                if(c.islower()):
                    priorityScore += ord(c) - ord('a') + 1
                else:
                    priorityScore += ord(c) - ord('A') + 27
                break

    print(f'The total priority is {priorityScore}')


totalPriority('input.txt')
