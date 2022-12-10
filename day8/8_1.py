def getVisibleTrees(filename):
    f = open(filename, 'r')

    grid = []

    for line in f:
        grid.append([int(c) for c in line.strip()])

    numVisible = 2 * len(grid) + 2 * len(grid[0]) - 4

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            checks = [
                [(k, j) for k in range(0, i)],
                [(k, j) for k in range(i+1, len(grid))],
                [(i, k) for k in range(0, j)],
                [(i, k) for k in range(j+1, len(grid[i]))]
            ]

            for r in checks:
                visible = True

                for k, l in r:
                    if(grid[k][l] >= grid[i][j]):
                        visible = False
                        break

                if(visible):
                    numVisible += 1
                    break

    print(f'The number of visible trees is {numVisible}')


getVisibleTrees('input.txt')
