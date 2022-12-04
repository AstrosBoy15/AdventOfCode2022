def calculateScore(filename):
    f = open(filename, 'r')

    scoreDict = {'X': 1, 'Y': 2, 'Z': 3}
    shapeHierarchy = {
        'X': {'Beats': 'C', 'Draws': 'A'},
        'Y': {'Beats': 'A', 'Draws': 'B'},
        'Z': {'Beats': 'B', 'Draws': 'C'}
    }

    score = 0

    for round in f:
        shapes = round.split()

        if(shapeHierarchy[shapes[1]]['Beats'] == shapes[0]):
            score += 6
        elif(shapeHierarchy[shapes[1]]['Draws'] == shapes[0]):
            score += 3

        score += scoreDict[shapes[1]]

    print(f'Your total score is {score}')


calculateScore('input.txt')
