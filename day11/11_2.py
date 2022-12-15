def getMonkeyBusiness(filename):
    f = open(filename, 'r')

    buffer = f.readlines()
    monkeys = []

    totalDivisor = 1

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

        totalDivisor *= monkey['test'][0]

        monkeys.append(monkey)

    monkeyInspections = [0 for i in range(len(monkeys))]

    for i in range(10000):
        for j in range(len(monkeys)):
            lhs = monkeys[j]['operation'][0]
            op = monkeys[j]['operation'][1]
            rhs = monkeys[j]['operation'][2]
            monkeyInspections[j] += len(monkeys[j]['items'])

            while len(monkeys[j]['items']) > 0:
                item = monkeys[j]['items'][0]
                del monkeys[j]['items'][0]

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

                if item % monkeys[j]['test'][0] == 0:
                    monkeys[monkeys[j]['test'][1]]['items'].append(
                        item % totalDivisor)
                else:
                    monkeys[monkeys[j]['test'][2]]['items'].append(
                        item % totalDivisor)

    activeMonkey1 = max(monkeyInspections)
    monkeyInspections.remove(activeMonkey1)
    activeMonkey2 = max(monkeyInspections)
    print(
        f'The level of monkey business in this situation is {activeMonkey1 * activeMonkey2}')


getMonkeyBusiness('input.txt')
