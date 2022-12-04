def getMaxCalories(filename):
    f = open(filename, 'r')
    maxCalories = 0
    currentCalories = 0

    for calorie in f:
        if(calorie == '\n'):
            if(currentCalories > maxCalories):
                maxCalories = currentCalories

            currentCalories = 0
        else:
            currentCalories += int(calorie)

    if(currentCalories > maxCalories):
        maxCalories = currentCalories

    print(f'The maximum calories possible is {maxCalories}')


getMaxCalories('input.txt')
