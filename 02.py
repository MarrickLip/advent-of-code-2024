_ = lambda *args: print(*args)

### Read Input
lines = list(open('./data/02.txt'))
reports = [
    [int(level) for level in report.strip().split(' ')]
      for report in lines
]

### Day 1
def is_valid(report):
    deltas = []
    for a, b in zip(report[:-1], report[1:]):
        deltas += [b-a]

    is_safe = all(d in (1, 2, 3) for d in deltas)
    is_safe = is_safe or all(-d in (1, 2, 3) for d in deltas)

    return is_safe
#print(sum(is_valid(report) for report in reports))

### Day 2
def is_valid(report):
    deltas = []
    for a, b in zip(report[:-1], report[1:]):
        deltas += [b-a]

    is_safe = all(d in (1, 2, 3) for d in deltas)
    is_safe = is_safe or all(-d in (1, 2, 3) for d in deltas)

    return is_safe

def is_valid_with_skip(report):
    if is_valid(report):
        return True
    
    is_valid_neg = True
    is_valid_pos = True
    for i, j in zip(range(0, len(report)-1), range(1, len(report))):
        if is_valid_pos:
            if report[j] - report[i] not in (1, 2, 3):
                without_i = [report[n] for n in range(len(report)) if n != i]
                without_j = [report[n] for n in range(len(report)) if n != j]
                #print((i, j), report[i], report[j], is_valid(without_i), is_valid(without_j))
                #print('without_i', without_i, is_valid(without_i))
                is_valid_pos = is_valid(without_i) or is_valid(without_j)
        if is_valid_neg:
            if report[j] - report[i] not in (-1, -2, -3):
                without_i = [report[n] for n in range(len(report)) if n != i]
                without_j = [report[n] for n in range(len(report)) if n != j]
                is_valid_neg = is_valid(without_i) or is_valid(without_j)
    return is_valid_neg or is_valid_pos

print(sum([is_valid_with_skip(report) for report in reports]))