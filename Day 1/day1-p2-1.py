words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Create a trie to search for numbers
trie = {}
for i, word in enumerate(words):
    curr = trie
    for char in word:
        if char not in curr:
            curr[char] = {}
        curr = curr[char]
    curr["$"] = i + 1


# Create intermediary with text replaced by numbers
with open("day1-p1-input.txt", "r") as f:
    with open("day1-p2-intermediate.txt", "w") as f2:
        for line in f:
            line = list(line)

            for i, char in enumerate(line):
                # Check if in trie
                if line[i] in trie:
                    j = i
                    curr = trie
                    found = None

                    while j < len(line):
                        if "$" in curr:
                            found = curr["$"]
                            break

                        elif line[j] in curr:
                            curr = curr[line[j]]
                            j += 1

                        else:
                            break

                    if found:
                        line[i] = str(found)

            f2.write("".join(line))
