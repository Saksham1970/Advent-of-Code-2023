with open("day3-p1-input.txt", "r") as f:
    with open("day3-p1-preprocess.txt", "w") as f2:
        length = len(f.readline()) - 1
        f.seek(0)
        blank = "." * length

        f2.write(blank + "\n")
        for line in f:
            f2.write(line)
        f2.write("\n" + blank)
