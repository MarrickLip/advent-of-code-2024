import re
string = open('./data/03.txt').read().strip()

### Part One
pattern = r'mul\((-?\d+),(-?\d+)\)'

total = 0
for x, y in re.findall(pattern, string):
    total += (int(x) * int(y))
print(total)


### Part Two
pattern = r"mul\((-?\d+),(-?\d+)\)|(do\(\))|(don't\(\))"

total = 0
enabled = True
for x, y, do, dont in re.findall(pattern, string):
    if do == 'do()':
        enabled = True
    elif dont == "don't()":
        enabled = False
    elif enabled:
        total += (int(x) * int(y))

print(total)
