def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    grid = []

    for line in lines:
        grid.append(list(line.strip()))

    return grid

def is_a_match(grid, x, y, letter):
    if (y < 0 or x < 0):
        return False
    elif (y >= len(grid) or x >= len(grid[y])):
        return False
    return grid[y][x] == letter

def is_start_of_xmas_dir(grid, x, y, dir):
    for (i, letter) in enumerate(["X", "M", "A", "S"]):
        new_x = x + (dir[0] * i)
        new_y = y + (dir[1] * i)
        if not is_a_match(grid, new_x, new_y, letter):
            return False
        
    return True

def is_start_of_xmas(grid, x, y):
    total_starts = 0
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        if (is_start_of_xmas_dir(grid, x, y, dir)):
            total_starts += 1
    
    return total_starts


coord_order = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def is_center_of_xmas_dir(grid, x, y, order_i):
    if (not is_a_match(grid, x, y, "A")):
        return False

    for (i, letter) in enumerate(["M", "M", "S", "S"]):
        coord_offset = coord_order[(order_i + i) % 4]
        new_x = x + coord_offset[0]
        new_y = y + coord_offset[1]
        if (not is_a_match(grid, new_x, new_y, letter)):
            return False

    return True

def is_center_of_xmas(grid, x, y):
    for rot in range(4):
        if (is_center_of_xmas_dir(grid, x, y, rot)):
            return True
    return False

def part_one(file):
    grid = parse_file(file)
    return sum (is_start_of_xmas(grid, x, y) for y in range(len(grid)) for x in range(len(grid[0])))

def part_two(file):
    grid = parse_file(file)
    return sum (is_center_of_xmas(grid, x, y) for y in range(len(grid)) for x in range(len(grid[0])))

if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))