def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    return list(map(int, lines[0].split()))

cached_vals = {}

def stones_after_blink(engraving):
    if (engraving == 0):
        return [1]
    
    if (engraving == 1):
        return [2024]
    
    num_s = str(engraving)
    l = len(num_s)
    if (l % 2 == 0):
        num_1 = int(num_s[0: l // 2])
        num_2 = int(num_s[l // 2:])
        return [num_1, num_2]
    
    return [engraving * 2024]

def blink_and_count(engraving, blinks_left):
    if (blinks_left == 0):
        return 1
    
    key = (engraving, blinks_left)
    if (not key in cached_vals):
        next_stones = stones_after_blink(engraving)
        cached_vals[key] = blink_and_count_all(next_stones, blinks_left - 1)

    return cached_vals[key]

def blink_and_count_all(stones, blinks_left):
    return sum(blink_and_count(engraving, blinks_left) for engraving in stones)

def part_one(stones):
    return blink_and_count_all(stones, 25)

def part_two(stones):
    return blink_and_count_all(stones, 75)

if __name__ == "__main__":
    stones = parse_file("input.txt")
    print(part_one(stones))
    print(part_two(stones))