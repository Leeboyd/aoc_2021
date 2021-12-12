from collections import defaultdict

with open('input/day12.txt') as f:
    data = [line.strip() for line in f]

def dfs(start, seen):
    if start == 'end':
        return 1

    s = 0
    for end in d[start]:
        if end not in seen:
            tmp = {end} if end.islower() else set()
            s += dfs(end, seen | tmp)
    
    return s


d = defaultdict(set)

for line in data:
    start, end = line.strip().split("-")
    d[start].add(end)
    d[end].add(start)

answer_1 = dfs("start", {"start"})
print(answer_1)