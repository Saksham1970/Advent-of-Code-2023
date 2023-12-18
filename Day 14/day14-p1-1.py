with open("day14-p1-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

dp = [[0] * len(grid[0]) for i in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            k = i - 1
            while True:
                if k < 0:
                    dp[i][j] = len(grid)
                    break
                elif grid[k][j] == "#":
                    dp[i][j] = len(grid) - 1 - k
                    break
                elif grid[k][j] == "O":
                    dp[i][j] = dp[k][j] - 1
                    break

                k -= 1


with open("day14-p1-output.txt", "w") as f:
    f.write(str(sum([sum(i) for i in dp])))
