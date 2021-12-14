import re
from collections import Counter, defaultdict

def run(n, template, rows):
    chars = defaultdict(int, Counter(template))
    template = Counter(zip(template, template[1:]))
    print(template)
    for _ in range(n):
        temp = defaultdict(int)
        for pair, count in template.items():
            chars[rows[pair]] += count
            temp[pair[0], rows[pair]] += count
            print(pair[0], rows[pair])
            print(temp)
            print('------')
            temp[rows[pair], pair[1]] += count
            print(temp)
            print('------ ------')
        template = temp
    return max(chars.values()) - min(chars.values())

with open('input/demo.txt') as f:
    template, rows = f.read().split('\n\n')

rows = re.findall(r'(\w+) -> (\w+)', rows)
rows = {tuple(pair): value for pair, value in rows}

run(1, 'NNCB', rows)
# run(40, template, rows)