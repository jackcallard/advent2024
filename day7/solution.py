directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]        

def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    board = []
    for (y, line) in enumerate(lines):
        row = list(line.strip());
        guard_x = row.index("^") if "^" in row else -1
        if (guard_x != -1):
            orig_x = guard_x
            orig_y = y
        board.append(row)

    return [board, orig_x, orig_y]

def get_key(x, y):
    return str(x) + "-" + str(y)

def get_key_with_direction(x, y, direction):
    return get_key(x, y) + "-" + str(direction)

def get_coords_from_key(key):
    return list(map(int, key.split("-")))

def coords_in_bounds(board, x, y):
    height = len(board)
    width = len(board[0])
    return 0 <= x < width and 0 <= y < height

def next_coords(x, y, direction):
    (add_x, add_y) = directions[direction]
    return (x + add_x, y + add_y)

def next_coords_blocked(board, x, y, direction):
    (next_x, next_y) = next_coords(x, y, direction)
    if (not coords_in_bounds(board, next_x, next_y)):
        return False
    return board[next_y][next_x] == "#"

def get_visited_coords(board, x, y):
    visited_coords = set()
    visited_coords_w_direction = set()
    direction = 0
    
    while (coords_in_bounds(board, x, y)):
        key_w_direction = get_key_with_direction(x, y, direction)
        if (key_w_direction in visited_coords_w_direction):
            return None
            
        visited_coords_w_direction.add(key_w_direction)
        visited_coords.add( get_key(x, y))
        while (next_coords_blocked(board, x, y, direction)):
            direction = (direction + 1) % 4
        (x, y) = next_coords(x, y, direction)

    return visited_coords

def part_one(board, x, y):
    visited_coords = get_visited_coords(board, x, y)
    return len(visited_coords)

def part_two(board, orig_x, orig_y):
    num_obstructions = 0
    possible_obstructions = get_visited_coords(board, orig_x, orig_y)

    for possible_obstruction in possible_obstructions:
        if (possible_obstruction == get_key(orig_x, orig_y)):
            continue
        [poss_x, poss_y] = get_coords_from_key(possible_obstruction)
        board[poss_y][poss_x] = "#"
        
        if (get_visited_coords(board, orig_x, orig_y) is None):
            num_obstructions += 1
       
        board[poss_y][poss_x] = "."

    return num_obstructions

if __name__ == "__main__":
    [board, orig_x, orig_y] = parse_file("input.txt")
    print(part_one(board, orig_x, orig_y))
    print(part_two(board, orig_x, orig_y))