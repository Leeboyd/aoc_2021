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

incomplete_score = {")": 1, "]": 2, "}": 3, ">": 4}

with open("input/day10.txt") as f:
    data = f.readlines()

answer1 = 0
answer2_candidates = []
for line in data:
    stack = []
    for c in line.strip():
        if c in ")}]>":
            if stack.pop() != maping_parenthesis[c]:
                answer1 += corrupted_score[c]
                break
        else:
            stack.append(c)
    else:
        score = 0
        for c in reversed(stack):
           score = score * 5 + incomplete_score[match_parenthesis[c]]
        answer2_candidates.append(score)

answer2 = sorted(answer2_candidates)[len(answer2_candidates) // 2]
print(answer1)
print(answer2)