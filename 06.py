grid = []

start_x = start_y = None

for i, raw_line in enumerate(open('./data/06.txt')):
    line = list(raw_line.strip())
    if '^' in line:
        start_x = line.index('^')
        start_y = i
        line[start_x] = '.'
    
    grid += [line]

grid_width = len(grid[0])
grid_height = len(grid)

print(grid_height, grid_width)
input('Continue?')

N = (+0, -1)
E = (+1, +0)
S = (+0, +1)
W = (-1, +0)

dx, dy = N
rotate = {
    N: E,
    E: S,
    S: W,
    W: N
}

def print_state(grid, visited, x, y, dx, dy):
    g = [[x for x in row] for row in grid]

    guard_char = {
        N: '^',
        E: '>',
        S: 'v',
        W: '<'
    }[(dx, dy)]

    for v_x, v_y in visited:
        g[v_y][v_x] = 'o'
    g[y][x] = guard_char

    for row in g:
        print(''.join(row))

    print('\n')

x, y = start_x, start_y
visited = set([(x, y)])
while True:
    x += dx
    y += dy

    if x < 0 or x > (grid_width - 1):
        break

    if y < 0 or y > (grid_height - 1):
        break

    if grid[y][x] == '#':
        x -= dx
        y -= dy
        dx, dy = rotate[(dx, dy)]
    else:
        visited.add((x, y))
        #print_state(grid, visited, x, y, dx, dy)

print(len(visited))

### Part Two

def is_loop(grid, x, y, dx_dy):
    dx, dy = dx_dy

    n_steps = 0
    while True:
        n_steps += 1

        x += dx
        y += dy

        if x < 0 or x > (grid_width - 1):
            return False

        if y < 0 or y > (grid_height - 1):
            return False

        if grid[y][x] == '#':
            x -= dx
            y -= dy
            dx, dy = rotate[(dx, dy)]
        
        if n_steps > (100 * grid_height * grid_width):
            return True
        
result = 0
for obs_x in range(0, grid_width):
    for obs_y in range(0, grid_height):
        if (obs_x, obs_y) == (start_x, start_y):
            continue

        if grid[obs_y][obs_x] == '#':
            continue

        g = [[cell for cell in row] for row in grid]
        g[obs_y][obs_x] = '#'

        print((obs_x, obs_y), end=' ')
        this_result = is_loop(g, start_x, start_y, N)
        print(this_result)
        result += int(this_result)

print(result)
