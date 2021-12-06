from collections import Counter
with open('./input/input6.txt', 'r') as f:
    fishes = Counter(map(int, f.read().split(',')))

def spawn_1(days, fishes):
    for _ in range(days):
        for fish_id in range(len(fishes)-1, -1, -1):
            fishes[fish_id] -= 1
            if fishes[fish_id] < 0:
                fishes[fish_id] = 6
                fishes.append(8)
    return len(fishes)

# Too Large!! Memory not enough
# print(spawn_1(256, fishes))

def spawn(day, fishes):
    for _ in range(day):
        new_fishes = {}
        for key, value in fishes.items():
            new_fishes[key - 1] = value
        new_fishes.pop(-1, None)
        if 0 in fishes:
            new_fishes[8] = fishes[0]
            new_fishes[6] = fishes[0] + new_fishes.get(6, 0)
        fishes = new_fishes
        
    return sum(new_fishes.values())

spawn(256, fishes)