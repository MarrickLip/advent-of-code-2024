
rules = []
updates = []
is_rules_section = True
for line in open('./data/05.txt'):
    if line.strip() == '':
        is_rules_section = False
    elif is_rules_section:
        a, b = line.strip().split('|')
        rules += [(int(a), int(b))]
    else:
        raw_updates = line.strip().split(',')
        updates += [tuple(int(page) for page in raw_updates)]


### Part One

incorrectly_ordered = []
result = 0 
for update in updates:
    indicies = {page: i for i, page in enumerate(update) }

    is_valid = True
    for x, y in rules:
        if x in indicies and y in indicies:
            if indicies[x] > indicies[y]:
                is_valid = False
                break

    if is_valid:
        middle_index = int((len(update) - 1) / 2)
        result += update[middle_index]
    else:
        incorrectly_ordered += [update]

print(result)

### Part Two
result = 0
rules = set(rules)
for original_update in incorrectly_ordered:
    update = list(original_update)

    for _ in range(len(update)):
        for i in range(0, len(update)-1):
            value_a, value_b = update[i], update[i+1]
            if (value_b, value_a) in rules:
                update[i+0], update[i+1] = update[i+1], update[i+0]

    middle_index = int((len(update) - 1) / 2)
    result += update[middle_index]

print(result)