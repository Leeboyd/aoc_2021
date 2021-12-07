from collections import Counter
with open('./input/input7.txt') as f:
    crab_data = Counter(map(int, f.read().split(',')))

def consume(crab_data, target):
    fuel = 0
    for current_location, count in crab_data.items():
        fuel = fuel + count * abs(target - current_location)
    return fuel

print(min([consume(crab_data, target) for target in crab_data.keys()]))

def consume_2(crab_data, target):
    fuel = 0
    for current_location, count in crab_data.items():
        range = abs(target - current_location)
        fuel = fuel + count * (range * (range + 1) / 2)
    return fuel

print(min([consume_2(crab_data, target) for target in crab_data.keys()]))