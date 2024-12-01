data = list(open('./in/01.txt'))

### Read Input
a = []
b = []
for line in data:
    raw_a, raw_b = line.strip().split('   ')
    
    a += [int(raw_a)]
    b += [int(raw_b)]

a = list(sorted(a))
b = list(sorted(b))

### Part One
distance = 0
for x, y in zip(a, b):
    distance += abs(x - y)

print('Part One:', distance)

### Part Two
result = 0
for x in a:
    n_times = sum(x == y for y in b)
    result += (x * n_times)

print('Part Two:', result)
