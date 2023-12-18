final_ans = 0

# Same as part 1 but with changed input
with open("day1-p2-intermediate.txt", "r") as f:
    for line in f:
        line_ans = 0

        for i in range(len(line)):
            if line[i].isnumeric():
                line_ans += int(line[i]) * 10
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                line_ans += int(line[i])
                break

        final_ans += line_ans

with open("day1-p2-output.txt", "w") as f:
    f.write(str(final_ans))
