def getMonkeyBusiness(filename):
    f = open(filename, 'r')

    buffer = f.readlines()
    monkeys = []

    for i in range(0, len(buffer), 7):
        monkey = {'items': [], 'operation': [], 'test': []}

        startingItems = buffer[i+1].strip()
        startingItems = startingItems.split(' ')

        for j in range(2, len(startingItems)):
            item = startingItems[j]
            if item[-1] == ',':
                item = item[:-1]

            monkey['items'].append(int(item))

        operation = buffer[i+2].strip()
        operation = operation.split(' ')

        monkey['operation'].append(operation[3])
        monkey['operation'].append(operation[4])
        monkey['operation'].append(operation[5])

        monkey['test'].append(int(buffer[i+3].strip().split(' ')[3]))
        monkey['test'].append(int(buffer[i+4].strip().split(' ')[5]))
        monkey['test'].append(int(buffer[i+5].strip().split(' ')[5]))

        monkeys.append(monkey)

    monkeyInspections = [0 for i in range(len(monkeys))]

    for i in range(20):
        for j, monkey in enumerate(monkeys):
            while len(monkey['items']) > 0:
                item = monkey['items'].pop(0)
                monkeyInspections[j] += 1

                lhs = monkey['operation'][0]
                op = monkey['operation'][1]
                rhs = monkey['operation'][2]

                if lhs == 'old':
                    leftVal = item
                else:
                    leftVal = int(lhs)

                if rhs == 'old':
                    rightVal = item
                else:
                    rightVal = int(rhs)

                if op == '+':
                    item = leftVal + rightVal
                else:
                    item = leftVal * rightVal

                item = int(item / 3)

                if item % monkey['test'][0] == 0:
                    monkeys[monkey['test'][1]]['items'].append(item)
                else:
                    monkeys[monkey['test'][2]]['items'].append(item)

    activeMonkey1 = max(monkeyInspections)
    monkeyInspections.remove(activeMonkey1)
    activeMonkey2 = max(monkeyInspections)
    print(
        f'The level of monkey business in this situation is {activeMonkey1 * activeMonkey2}')


getMonkeyBusiness('input.txt')
