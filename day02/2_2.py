def calculateScore(filename):
    f = open(filename, 'r')

    scorePlayedDict = {'A': 1, 'B': 2, 'C': 3}
    scoreOutcomeDict = {'X': 0, 'Y': 3, 'Z': 6}
    shapeHierarchy = {
        'A': {'X': 'C', 'Y': 'A', 'Z': 'B'},
        'B': {'X': 'A', 'Y': 'B', 'Z': 'C'},
        'C': {'X': 'B', 'Y': 'C', 'Z': 'A'}
    }

    score = 0

    for round in f:
        shapes = round.split()
        shapePlayed = shapeHierarchy[shapes[0]][shapes[1]]

        score += scoreOutcomeDict[shapes[1]] + scorePlayedDict[shapePlayed]

    print(f'Your total score is {score}')


calculateScore('input.txt')
