match_parenthesis = {
    "(":")",
    "{":"}",
    "[":"]",
    "<":">"
}

maping_parenthesis = {
    "}":"{",
    ")":"(",
    "]":"[",
    ">":"<"
}

corrupted_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

with open("input/day10.txt") as f:
    data = f.readlines()

answer1 = 0
for line in data:
    stack = []
    for c in line.strip():
        if c in ")}]>":
            if stack.pop() != maping_parenthesis[c]:
                answer1 += corrupted_score[c]
                break
        else:
            stack.append(c)

print(answer1)