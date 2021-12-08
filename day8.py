import re
from collections import Counter

with open('./input/input8.txt') as f:
    lines = sum([line.split(" | ")[1].split(" ") for line in f.read().rstrip().split('\n')], [])
    lines_counter = Counter(map(len, lines))

# answer 1
print(lines_counter.get(2) + lines_counter.get(4) + lines_counter.get(3) + lines_counter.get(7))