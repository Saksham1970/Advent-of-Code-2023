from collections import OrderedDict
import re
import pickle

switch = False
workflows = {}
parts = []

with open("day19-p1-input.txt", "r") as f:
    for i in f.readlines():
        if i.strip() == "":
            switch = True
            continue

        if switch:
            parts.append(
                eval(
                    re.sub(
                        pattern=r"([xmas])",
                        repl=r"'\1'",
                        string=i.strip().replace("=", ":"),
                    )
                )
            )

        else:
            workflow_name = re.sub(r"{.*}", r"", i.strip())
            workflow = re.search(r"{.*}", i.strip()).group(0)
            workflow = re.sub(r"(?<![\w><])([\w><]+)(?![\w><])", r"'\1'", workflow)
            workflow = "OrderedDict(" + workflow[:-1] + ": None})"
            workflows[workflow_name] = eval(workflow)


def is_accepted(part):
    workflow = workflows["in"]
    end = False
    accept = False
    while not end:
        for condition in workflow:
            if workflow[condition]:
                if eval(condition, {}, part):
                    if workflow[condition] in "AR":
                        if workflow[condition] == "A":
                            accept = True
                        end = True
                    else:
                        workflow = workflows[workflow[condition]]
                    break
            else:
                if condition in "AR":
                    if condition == "A":
                        accept = True
                    end = True
                else:
                    workflow = workflows[condition]
                break
    return accept


res = 0
for part in parts:
    if is_accepted(part):
        res += sum(part.values())

pickle.dump(workflows, open("day19-p2-intermediate.obj", "wb"))

open("day19-p1-output.txt", "w").write(str(res))
