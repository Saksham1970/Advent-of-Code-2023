final_ans = 0

with open("day1-p1-input.txt", "r") as f:
    for line in f:
        line_ans = 0

        # First number from left
        for i in range(len(line)):
            if line[i].isnumeric():
                line_ans += int(line[i]) * 10
                break

        # First number from right
        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                line_ans += int(line[i])
                break

        final_ans += line_ans

with open("day1-p1-output.txt", "w") as f:
    f.write(str(final_ans))
