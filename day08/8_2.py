def getBestVisiblity(filename):
    f = open(filename, 'r')

    grid = []

    for line in f:
        grid.append([int(c) for c in line.strip()])

    bestScore = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            checks = [
                [(k, j) for k in range(i-1, -1, -1)],
                [(k, j) for k in range(i+1, len(grid))],
                [(i, k) for k in range(j-1, -1, -1)],
                [(i, k) for k in range(j+1, len(grid[i]))]
            ]

            visibility = 1

            for r in checks:
                for k, l in r:
                    if(grid[k][l] >= grid[i][j]):
                        break

                visibility *= (abs(k-i) + abs(l-j))

            bestScore = max(bestScore, visibility)

    print(f'The score of visible trees is {bestScore}')


getBestVisiblity('input.txt')
