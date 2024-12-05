grid = [line.strip() for line in open('./data/04.txt')]

grid_width = len(grid[0])
grid_height = len(grid)

### Part One

def is_match(start_x, start_y, dx, dy):
    x = start_x
    y = start_y

    chars_to_find = list('XMAS')
    while len(chars_to_find):
        if x < 0 or x > (grid_width-1):
            return False
        
        if y < 0 or y > (grid_height-1):
            return False

        if grid[y][x] != chars_to_find[0]:
            return False
        
        x += dx
        y += dy

        chars_to_find = chars_to_find[1:]

    return True

n_matches = 0
for x in range(0, grid_width):
    for y in range(0, grid_height):
        if grid[y][x] != 'X':
            continue
        #print()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                #print((x, y), (dx, dy), is_match(x, y, dx, dy))
                n_matches += int(is_match(x, y, dx, dy))

print(n_matches)

### Part Two

row_padding = '*' * (grid_width+2)
grid = [row_padding] + ['*'+row+'*' for row in grid] + [row_padding]

n_matches = 0
for x in range(1, grid_width+1):
    for y in range(1, grid_height+1):
        if grid[y][x] != '&':
            if grid[y][x] == 'A':
                is_cross_a = {grid[y+1][x+1], grid[y-1][x-1]} == {'M', 'S'}
                is_cross_b = {grid[y+1][x-1], grid[y-1][x+1]} == {'M', 'S'}

                if is_cross_a and is_cross_b:
                    n_matches += 1
print(n_matches)
        

