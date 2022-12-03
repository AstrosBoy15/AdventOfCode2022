def swapValues(calories):
    for i in range(3):
        if(calories[i] > calories[i+1]):
            temp = calories[i]
            calories[i] = calories[i+1]
            calories[i+1] = temp

    return calories


def getTopCalories(filename):
    f = open(filename, 'r')
    maxCalories = [0, 0, 0, 0]

    for calorie in f:
        if(calorie == '\n'):
            maxCalories = swapValues(maxCalories)
            maxCalories[0] = 0
        else:
            maxCalories[0] += int(calorie)

    maxCalories = swapValues(maxCalories)
    maxCalories.pop(0)
    print('The maximum calories possible is ' + str(sum(maxCalories)))


getTopCalories('input.txt')
