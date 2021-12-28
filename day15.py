# from itertools import product
import heapq
with open("input/day15.txt") as f:
    lines = [list(map(int, line)) for line in f.read().rstrip().split("\n")]

def is_valid(lines, x, y):
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    return True

# def get_adjacent(lines, i, j):
#     for dy, dx in product([-1, 0, 1], repeat=2):
#         i1, j1 = i + dy, j + dx
#         if 0 <= i1 < len(lines) and 0 <= j1 < len(lines[0]):
#             yield i1, j1

def get_adjacent(lines, x, y):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        x1, y1 = x + dx, y + dy
        if is_valid(lines, x1, y1):
            yield y1, x1

def shortest_distance(lines):
    destination = len(lines[-1]) - 1, len(lines) - 1
    heap = [(0, (0, 0))] # tuple compared position by position
    seen = {(0, 0)} # prevent visited more than one time
    while heap:
        dist, (y, x) = heapq.heappop(heap)
        if (y, x) == destination:
            return dist
        
        for _y, _x in get_adjacent(lines, x, y):
            if (_y, _x) in seen:
                continue
            heapq.heappush(heap, (dist + lines[_y][_x], (_y, _x)))
            seen.add((_y,_x))

def scaling(times, datas):
    expand_data = [line * times for line in datas * times]
    height = len(datas)
    width = len(datas[0])
    expand_height = len(expand_data)
    expand_width = len(expand_data[0])
    for i in range(expand_height):
        for j in range(expand_width):
            expand_data[i][j] = (expand_data[i][j] + i // height + j // width - 1) % 9 + 1
    return expand_data

answer_1 = shortest_distance(lines)

new_lines = scaling(5, lines)

print(answer_1)

answer_2 = shortest_distance(new_lines)

print(answer_2)