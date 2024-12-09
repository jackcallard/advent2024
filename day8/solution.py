import math

def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid

def coords_in_bounds(coords, grid):
    height = len(grid)
    width = len(grid[0])
    return 0 <= coords[0] < width and 0 <= coords[1] < height

def previous_coords(coords, run, rise):
    return (coords[0] - run, coords[1] - rise) 

def next_coords(coords, run, rise):
    return (coords[0] + run, coords[1] + rise) 

def get_antinode_locations(coordA, coordB, grid, perpetuate):
    rise = coordB[1] - coordA[1]
    run = coordB[0] - coordA[0]

    if (not perpetuate):
        return filter(lambda coords: coords_in_bounds(coords, grid), 
                      [previous_coords(coordA, run, rise), next_coords(coordB, run, rise)])
    
    locations = []
    divisor = math.gcd(rise, run)
    new_rise = rise // divisor
    new_run = run // divisor

    curr_coords = coordA
    while (coords_in_bounds(curr_coords, grid)):
        locations.append(curr_coords)
        curr_coords = previous_coords(curr_coords, new_run, new_rise)

    curr_coords = next_coords(coordA, new_run, new_rise)
    while(coords_in_bounds(curr_coords, grid)):
        locations.append(curr_coords)
        curr_coords = next_coords(curr_coords, new_run, new_rise)

    return locations

def create_antenna_map(grid):
    antenna_map = {}
    for (y, row) in enumerate(grid):
        for (x, elm) in enumerate(row):
            if elm == ".":
                continue
            coords = antenna_map.get(elm, [])
            coords.append((x, y))
            antenna_map[elm] = coords
    
    return antenna_map

def calc_num_antinodes(grid, perpetuate):
    antenna_map = create_antenna_map(grid)
    antinode_locations = set()
    
    for key in antenna_map:
        coords = antenna_map[key]
        for (i, coord) in enumerate(coords):
            for j in range(i + 1, len(coords)):
                locations = get_antinode_locations(coord, coords[j], grid, perpetuate)
                for loc in locations: antinode_locations.add(loc)

    return len(antinode_locations)

def part_one(grid):
    return calc_num_antinodes(grid, False)

def part_two(grid):
    return calc_num_antinodes(grid, True)

if __name__ == "__main__":
    grid = parse_file("input.txt")
    print(part_one(grid))
    print(part_two(grid))