def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    first_list = []
    second_list = []

    for line in lines:
        [first, second] = line.split()
        first_list.append(int(first))
        second_list.append(int(second))

    return [first_list, second_list]


def part_one(file):
    [first_list, second_list] = parse_file(file)
        
    first_list.sort()
    second_list.sort()

    sum = 0
    for i in range(len(first_list)):
        sum += abs(first_list[i] - second_list[i])
    
    return sum

def part_two(file):
    [first_list, second_list] = parse_file(file)

    freq_map = {}
    for num in second_list:
        freq = freq_map.get(num, 0);
        freq_map[num] = freq + 1

    sum = 0
    for num in first_list:
        freq = freq_map.get(num, 0)
        sum += (num * freq)

    return sum

if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))