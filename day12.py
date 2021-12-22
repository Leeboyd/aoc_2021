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

def dfs_2(start, seen, as_start=False):
    if start == 'end':
        return 1

    s = 0
    for end in d[start]:
        if end not in seen:
            tmp = {end} if end.islower() else set()
            s += dfs_2(end, seen | tmp, as_start)
        elif as_start and end != "start":
            s += dfs_2(end, seen, False)
    return s

d = defaultdict(set)

for line in data:
    start, end = line.strip().split("-")
    d[start].add(end)
    d[end].add(start)

# small caves can be only visited once
answer_1 = dfs("start", {"start"})
print(answer_1)
# small caves can be visited 2 times
answer_2 = dfs_2("start", {"start"}, True)
print(answer_2)