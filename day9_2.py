'''REFERENCE
__author__ = "James-Ansley"
__url__ = "https://github.com/James-Ansley/adventofcode/"
'''
from itertools import product
from collections import deque
from math import prod

with open('input/input9.txt') as f:
    data = [[int(value) for value in line.strip()] for line in f]

def get_adjacent(data, i, j):
    adjacent = []
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        i1, j1 = i + dy, j + dx
        if 0 <= i1 < len(data) and 0 <= j1 < len(data[0]):
            adjacent.append((i1, j1))
    return adjacent

def bfs(data, i, j):
    visited = [(i, j)]
    queue = deque(((i,j),))
    while queue:
        i, j = queue.pop()
        for i1, j1 in get_adjacent(data, i, j):
            if (i1, j1) not in visited and data[i1][j1] != 9:
                queue.appendleft((i1, j1))
                visited.append((i1,j1))
    return len(visited)

basin = []
for i,j in product(range(len(data)), range(len(data[0]))):
    adjacent = get_adjacent(data, i, j)
    if all(data[i][j]< data[i1][j1] for i1, j1 in adjacent):
        # 確認為低點才進此, 
        # 求低點所屬 basin, basin: 9 圍起來的面積
        basin.append(bfs(data, i,j))

basin.sort()
print(prod(basin[-3:]))