from copy import deepcopy
import pickle

workflows = pickle.load(open("day19-p2-intermediate.obj", "rb"))

res = [0]


def dfs(mins, maxs, workflow):
    end = False
    accept = False
    while not end:
        for condition in workflow:
            if workflow[condition]:
                category = condition[0]
                operator = condition[1]
                operand = int(condition[2:])
                mins2, maxs2 = deepcopy(mins), deepcopy(maxs)

                if operator == ">":
                    mins2[category] = max(mins2[category], operand + 1)
                    maxs[category] = min(maxs[category], operand)
                else:
                    maxs2[category] = min(maxs2[category], operand - 1)
                    mins[category] = max(mins[category], operand)

                if workflow[condition] in "AR":
                    if workflow[condition] == "A":
                        ways = 1
                        for category in mins2:
                            ways *= max(0, maxs2[category] - mins2[category] + 1)

                        res[0] += ways
                else:
                    dfs(mins2, maxs2, workflows[workflow[condition]])

            else:
                if condition in "AR":
                    if condition == "A":
                        accept = True
                    end = True
                else:
                    workflow = workflows[condition]

    if accept:
        ways = 1
        for category in mins:
            ways *= max(0, maxs[category] - mins[category] + 1)

        res[0] += ways


mins = {"x": 1, "m": 1, "a": 1, "s": 1}
maxs = {"x": 4000, "m": 4000, "a": 4000, "s": 4000}
workflow = workflows["in"]

dfs(mins, maxs, workflow)

open("day19-p2-output.txt", "w").write(str(res[0]))
