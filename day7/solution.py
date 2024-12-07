def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    equations = []
    for line in lines:
        [result_str, numbers_str] = line.split(":")

        result = int(result_str)
        numbers = list(map(int, numbers_str.split()))

        equations.append((result, numbers))

    return equations

def result_possible(curr_val, goal_val, numbers, concat_allowed):
    if (curr_val == goal_val and len(numbers) == 0):
        return True
    if (curr_val > goal_val):
        return False
    if (len(numbers) == 0):
        return False
    
    first_val = numbers[0]
    next_numbers = numbers[1:]

    add_possible = result_possible(curr_val + first_val, goal_val, next_numbers, concat_allowed)
    if add_possible:
        return True
    
    mult_possible = result_possible(curr_val * first_val, goal_val, next_numbers, concat_allowed)
    if mult_possible:
        return True
    
    return concat_allowed and result_possible(int(str(curr_val) + str(first_val)), goal_val, next_numbers, concat_allowed)


def sum_possible(equations, concat_allowed):
    sum = 0
    for (result, numbers) in equations:
        if (result_possible(numbers[0], result, numbers[1:], concat_allowed)):
            sum += result
    return sum


def part_one(equations):
    return sum_possible(equations, False)

def part_two(equations):
    return sum_possible(equations, True)

if __name__ == "__main__":
    equations = parse_file("input.txt")
    print(part_one(equations))
    print(part_two(equations))