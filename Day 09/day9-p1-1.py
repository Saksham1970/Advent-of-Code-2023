sum_ = 0
with open("day9-p1-input.txt", "r") as f:
    for line in f:
        nums = [int(i) for i in line.split()]

        for i in range(len(nums), 1, -1):
            for j in range(1, i):
                nums[j - 1] = nums[j] - nums[j - 1]
        sum_ += sum(nums)

with open("day9-p1-output.txt", "w") as f:
    f.write(str(sum_))
