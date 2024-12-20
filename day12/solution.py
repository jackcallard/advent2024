horizontal_directions = [(1, 0), (-1, 0)]
vertical_directions = [(0, -1), (0, 1)]
directions = horizontal_directions + vertical_directions

def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    garden = []
    for line in lines:
        garden.append(list(line.strip()))

    return garden

def get_plot_type_of_coords(coords, garden):
    return garden[coords[1]][coords[0]]

def coords_in_bound(coords, garden):
    return 0 <= coords[0] < len(garden[0]) and 0 <= coords[1] < len(garden)

def coords_have_plot_type(coords, plot_type, garden):
    return coords_in_bound(coords, garden) and get_plot_type_of_coords(coords, garden) == plot_type

def get_next_coords(curr_coords, direction):
    (add_x, add_y) = direction
    return (curr_coords[0] + add_x, curr_coords[1] + add_y)

def get_coords_to_visit(coords, garden):
    neighbors = []
    plot_type = get_plot_type_of_coords(coords, garden)
    for direction in directions:
        coords_to_check = get_next_coords(coords, direction)
        if coords_have_plot_type(coords_to_check, plot_type, garden):
            neighbors.append(coords_to_check)
    return neighbors

def get_plot_coords(starting_coords, garden):
    plot_coords = {starting_coords}
    coords_to_visit = set(get_coords_to_visit(starting_coords, garden))
    while len(coords_to_visit):
        curr_coords = coords_to_visit.pop()
        if (curr_coords in plot_coords):
            continue

        plot_coords.add(curr_coords)
        coords_neighbors = get_coords_to_visit(curr_coords, garden)
        coords_to_visit = coords_to_visit.union(coords_neighbors)

    return plot_coords

def count_of_lists_of_map(map_of_lists, dedup_sequential_nums):
    total = 0
    for key in map_of_lists:
        l = map_of_lists[key]
        if dedup_sequential_nums:
            l_sorted = sorted(l)
            total += sum([i == 0 or l_sorted[i - 1] + 1 != num for (i, num) in enumerate(l_sorted)])
        else:
            total += len(l)
    return total

def get_plot_perimeter(plot_coords, garden, bulk_discount):
    border_col_by_row_and_dir = {}
    border_row_by_col_and_dir = {}

    for coords in plot_coords:
        plot_type = get_plot_type_of_coords(coords, garden)
        
        for horizontal_d in horizontal_directions:
            coords_to_check = get_next_coords(coords, horizontal_d)
            if not coords_have_plot_type(coords_to_check, plot_type, garden):
                key = (coords[0], horizontal_d)
                col_coords = border_row_by_col_and_dir.get(key, [])
                col_coords.append(coords[1])
                border_row_by_col_and_dir[key] = col_coords
        
        for vertical_d in vertical_directions:
            coords_to_check = get_next_coords(coords, vertical_d)
            if not coords_have_plot_type(coords_to_check, plot_type, garden):
                key = (coords[1], vertical_d)
                row_coords = border_col_by_row_and_dir.get(key, [])
                row_coords.append(coords[0])
                border_col_by_row_and_dir[key] = row_coords

    return count_of_lists_of_map(border_row_by_col_and_dir, bulk_discount) + count_of_lists_of_map(border_col_by_row_and_dir, bulk_discount);

def calculate_cost(garden, bulk_discount):
    sum = 0
    coords_not_visited = set([(x, y) for y in range(len(garden)) for x in range(len(garden[y]))])
    
    while len(coords_not_visited):
        starting_coords = coords_not_visited.pop()
        plot_coords = get_plot_coords(starting_coords, garden)
        coords_not_visited = coords_not_visited.difference(plot_coords)
        sum += get_plot_perimeter(plot_coords, garden, bulk_discount) * len(plot_coords)
        
    return sum

def part_one(garden):
    return calculate_cost(garden, False)

def part_two(garden):
    return calculate_cost(garden, True)

if __name__ == "__main__":
    g = parse_file("input.txt")
    print(part_one(g))
    print(part_two(g))