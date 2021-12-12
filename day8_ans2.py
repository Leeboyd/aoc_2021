from itertools import permutations

with open("./input/input8.txt") as f:
    data = f.readlines()

# 已知 MAPPING
d = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

# part_1 = 0
part_2 = 0
for line_ind, line in enumerate(data):
    a, b = line.split(" | ")
    # pattern
    a = a.split()
    # output
    b = b.split()
    # part_1 += sum(len(code) in {2, 3, 4, 7} for code in b)
    # 窮舉組合  
    for perm_ind, permutation in enumerate(permutations("abcdefg")):
        to = str.maketrans("abcdefg", "".join(permutation))
        a_ = ["".join(sorted(code.translate(to))) for code in a]
        b_ = ["".join(sorted(code.translate(to))) for code in b]
        
        # a 的排列組合是否有 MAPPING
        if all(code in d for code in a_):
            part_2 += int("".join(str(d[code]) for code in b_))
            break

# print(part_1)
print(part_2)