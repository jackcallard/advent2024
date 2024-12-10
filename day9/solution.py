def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    blocks = []
    disk_map = lines[0].strip()
    for i in range(0, len(disk_map)):
        size = int(disk_map[i])
        id = i // 2 if i % 2 == 0 else "."
        for _ in range(size): blocks.append(id)
    return blocks

def get_checksum(blocks):
    return sum(i * id if id != "." else 0 for i, id in enumerate(blocks))

def find_open_spot(id, size, blocks):
    i = 0
    curr_spot_size = 0
    while (blocks[i] != id):
        if blocks[i] == ".":
            curr_spot_size += 1
        else:
            curr_spot_size = 0
        
        if (curr_spot_size == size):
            return i - curr_spot_size + 1
        
        i += 1
    
    return -1

def swap_elements(first, second, blocks):
    tmp = blocks[second]
    blocks[second] = blocks[first]
    blocks[first] = tmp

def swap_range(first, second, size, blocks):
    for i in range(size): swap_elements(first + i, second + i, blocks)

def part_one(blocks):
    blocks = list(blocks)
    left = 0
    right = len(blocks) - 1
    while True:
        while blocks[left] != ".":
            left += 1
        while blocks[right] == ".":
            right -= 1
        if (left >= right):
            break
        
        swap_elements(left, right, blocks)
    
    return get_checksum(blocks)

def part_two(blocks):
    blocks = list(blocks)
    i = len(blocks) - 1
    while True:
        while i >= 0 and blocks[i] == ".": 
            i -= 1
        if i <= 0: 
            break
        
        id = blocks[i]
        size = 1
        
        while (i - size >= 0 and blocks[i - size] == id): 
            size += 1

        swap_i = find_open_spot(id, size, blocks)
        start_i = i - size + 1

        if (swap_i != -1): 
            swap_range(swap_i, start_i, size, blocks)
        
        i -= size
    
    return get_checksum(blocks)

if __name__ == "__main__":
    blocks = parse_file("input.txt")
    print(part_one(blocks))
    print(part_two(blocks))