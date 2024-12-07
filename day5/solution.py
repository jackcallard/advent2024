def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    dependencies = {}
    updates = []

    first_half = True
    for line in lines:
        if (line.strip() == ""):
            first_half = False
        elif (first_half):
            [first, second] = map(int, line.split("|"))
            entry = dependencies.get(second, set())
            entry.add(first)
            dependencies[second] = entry
        else:
            update = list(map(int, line.split(",")))
            updates.append(update)

    return [updates, dependencies]

def get_relevant_deps(page_num, dependencies, nums_to_care_about):
    page_deps = dependencies.get(page_num, set())
    return set(filter(lambda x: x in nums_to_care_about, page_deps))

def index_with_no_deps(update, dependencies):
    for (i, page_num) in enumerate(update):
        relevant_deps = get_relevant_deps(page_num, dependencies, update)
        if (len(relevant_deps) == 0):
            return i
    return -1

def topo_sort(update, dependencies):
    sorted = []
    remaining = list(update)
    while (remaining):
        next_i = index_with_no_deps(remaining, dependencies)
        if (next_i == -1):
            raise "Cannot find elem with no deps"
        sorted.append(remaining.pop(next_i))
        
    return sorted

def valid_update(update, dependencies):
    seen_nums = set()
    reversed_update = reversed(update)
    for page_num in reversed_update:
        conflicting_deps = get_relevant_deps(page_num, dependencies, seen_nums)
        if (len(conflicting_deps)):
            return False
        seen_nums.add(page_num)
        
    return True

def part_one(updates, dependencies):
    sum = 0
    for update in updates:
        if (valid_update(update, dependencies)):
            middle_num = update[len(update) // 2]
            sum += middle_num

    return sum

def part_two(updates, dependencies):
    sum = 0
    for update in updates:
        if (not valid_update(update, dependencies)):
            sorted_update = topo_sort(update, dependencies)
            middle_num = sorted_update[len(sorted_update) // 2]
            sum += middle_num

    return sum

if __name__ == "__main__":
    [updates, dependencies] = parse_file("input.txt")
    print(part_one(updates, dependencies))
    print(part_two(updates, dependencies))