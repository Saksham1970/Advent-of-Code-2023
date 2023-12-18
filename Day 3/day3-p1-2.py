# Only keeping 3 lines of file in working to minimise space used
working_set = [[]]

res = 0

with open("day3-p1-preprocess.txt", "r") as f:
    a = f.readline()
    length = len(a)
    working_set.append(list(a))
    working_set.append(list(f.readline()))

    for line in f:
        working_set.pop(0)
        working_set.append(list(line))

        curr = working_set[1]
        i = 0
        while i < length:
            if curr[i].isnumeric():
                j = i
                while j < length and curr[j].isnumeric():
                    j += 1

                if (
                    # if left is special
                    (curr[max(0, i - 1)] != "." and not curr[max(0, i - 1)].isnumeric())
                    # if right is special
                    or (curr[j] != "." and not curr[j].isnumeric())
                    # if top is special
                    or (
                        working_set[0][max(0, i - 1) : j + 1].count(".")
                        != j - max(0, i - 1) + 1
                    )
                    # if bottom is special
                    or (
                        working_set[2][max(0, i - 1) : j + 1].count(".")
                        != j - max(0, i - 1) + 1
                    )
                ):
                    num = int("".join(curr[i:j]))
                    res += num
                i = j
            else:
                i += 1

with open("day3-p1-output.txt", "w") as f:
    f.write(str(res))
