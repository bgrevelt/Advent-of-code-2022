'''This is an ugly one, I had trouble getting numpy to install and
figured I would just bodge something together that works'''

test_input = '''30373
25512
65332
33549
35390'''

def create_height_grid(txt):
    return [[int(c) for c in line] for line in txt.splitlines()]

def get_visible_trees(grid, startat_x, startat_y, step_x, step_y):
    heighest = -1
    visible = []
    x = startat_x
    y = startat_y
    while len(grid) > y >= 0 and len(grid[y]) > x >= 0:
        if grid[y][x] > heighest:
            heighest = grid[y][x]
            visible.append((x,y))
        x += step_x
        y += step_y
    return visible

def get_all_visible_trees(grid):
    height = len(grid)
    width = len(grid[0])

    visible = set()

    for n in range(width):
        visible = visible.union(get_visible_trees(grid, 0, n, 1, 0))
        visible = visible.union(get_visible_trees(grid, width - 1, n, -1, 0))
    for n in range(height):
        visible = visible.union(get_visible_trees(grid, n, 0, 0, 1))
        visible = visible.union(get_visible_trees(grid, n, height - 1, 0, -1))
    return visible

def puzzle1(input):
    grid = create_height_grid(input)
    return len(get_all_visible_trees(grid))


assert puzzle1(test_input) == 21, "With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement."

with open('input.txt') as f:
    print(puzzle1(f.read()))

def get_viewing_distance(grid, startx, starty, dx, dy):
    x=startx+dx
    y=starty+dy
    my_height = grid[starty][startx]

    while len(grid) > y >= 0 and len(grid[y]) > x >= 0:
        #print(x,y, grid[y][x])
        if grid[y][x] >= my_height:
            return max(abs(x-startx), abs(y-starty))
        x += dx
        y += dy

    # If we get here, we reached the edge
    return max(abs(x - startx - dx), abs(y - starty - dy))

def get_scening_score(grid, x, y):
    a = get_viewing_distance(grid, x, y, 0, -1)
    b = get_viewing_distance(grid, x, y, -1, 0)
    c = get_viewing_distance(grid, x, y, 1, 0)
    d = get_viewing_distance(grid, x, y, 0, 1)

    return a*b*c*d

assert get_scening_score(create_height_grid(test_input), 2, 1) == 4, "For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2)."
assert get_scening_score(create_height_grid(test_input), 2, 3) == 8, "This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house."

def get_max_scening_score(grid):
    height = len(grid)
    width = len(grid[0])
    return max(get_scening_score(grid, col, row) for row in range(height) for col in range(width))

assert get_max_scening_score(create_height_grid(test_input)) == 8, "This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house."

def puzzle2(input):
    grid = create_height_grid(input)
    return get_max_scening_score(grid)

with open('input.txt') as f:
    print(puzzle2(f.read()))