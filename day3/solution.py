def parse_file(file):
    file1 = open(file, 'r')
    return file1.read()

def get_value(file_string, index):
    closing_paren = file_string.find(")", index + 1)
    if (closing_paren == -1):
        return 0
    
    contents = file_string[index + len("mul("): closing_paren]
    if (contents.count(",") != 1 or " " in contents or "\n" in contents):
        return 0
    
    try:
        [first_int, second_int] = map(int, contents.split(","))
    except:
        return 0
    
    if (first_int >= 1000 or second_int >= 1000):
        return 0
    
    return first_int * second_int

def get_total_value(file_string, always_enabled):
    enabled = True
    sum = i = 0
    while(i < len(file_string)):
        if (always_enabled or enabled) and file_string[i: i + len("mul(")] == "mul(":
            sum += get_value(file_string, i)
        elif (file_string[i: i + len("do()")] == "do()"):
            enabled = True
        elif (file_string[i: i + len("don't()")] == "don't()"):
            enabled = False
        i += 1

    return sum

def part_one(file):
    file_string = parse_file(file)
    return get_total_value(file_string, True)

def part_two(file):
    file_string = parse_file(file)
    return get_total_value(file_string, False)

if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))