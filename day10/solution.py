def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    grid = []
    trail_heads = []

    for (y, line) in enumerate(lines):
        row = []
        for (x, elm) in enumerate(list(line.strip())):
            if (elm == "."):
                row.append(-1)
            elif (elm == "0"):
                row.append(0)
                trail_heads.append((x, y))
            else:
                row.append(int(elm))
        grid.append(row)
    return (grid, trail_heads)

def coords_in_bounds(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def coords_has_height(x, y, height, grid):
    return coords_in_bounds(x, y, grid) and height == grid[y][x]

def valid_next_steps(x, y, grid):
    curr_height = grid[y][x]
    poss_next_coords = [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]
    return filter(lambda coords: coords_has_height(coords[0], coords[1], curr_height + 1, grid), poss_next_coords)
    
# return all peaks that can be reached from (x, y), duplicates indicating an extra path to the peak
def find_peaks(x, y, grid):
    if (grid[y][x] == 9):
        return {(x, y)}

    found_peaks = []
    for valid_step in valid_next_steps(x, y, grid):
        (new_x, new_y) = valid_step
        found_peaks.extend(find_peaks(new_x, new_y, grid))

    return found_peaks

def part_one(grid, trail_heads):
    sum = 0
    for trail_head in trail_heads:
        (x, y) = trail_head
        sum += len(set(find_peaks(x, y, grid)))
    return sum

def part_two(grid, trail_heads):
    sum = 0
    for trail_head in trail_heads:
        (x, y) = trail_head
        sum += len(find_peaks(x, y, grid))
    return sum

if __name__ == "__main__":
    (grid, trail_heads) = parse_file("input.txt")
    print(part_one(grid, trail_heads))
    print(part_two(grid, trail_heads))