from itertools import product

with open('input/input9.txt') as f:
    data = [[int(value) for value in line.strip()] for line in f]

def get_adjacent(data, i, j):
    adjacent = []
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        i1, j1 = i + dy, j + dx
        if 0 <= i1 < len(data) and 0 <= j1 < len(data[0]):
            adjacent.append((i1, j1))
    return adjacent

risk = []
for i,j in product(range(len(data)), range(len(data[0]))):
    adjacent = get_adjacent(data, i, j)
    if all(data[i][j]< data[i1][j1] for i1, j1 in adjacent):
        risk.append(data[i][j] + 1)

print(sum(risk))