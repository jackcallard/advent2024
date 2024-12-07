def parse_file(file):
    file1 = open(file, 'r')
    lines = file1.readlines()

    reports = []

    for line in lines:
        report = list(map(int, line.split()))
        reports.append(report)

    return reports

def report_safe(report, can_omit):
    is_asc = report[1] > report[0]
    for i in range(len(report) - 1):
        [val, next_val] = report[i : i + 2]
        if (abs(next_val - val) > 3):
            return can_omit and try_with_omission(report, i)
        if (next_val == val):
            return can_omit and try_with_omission(report, i)
        if ((next_val > val) != is_asc):
            return can_omit and try_with_omission(report, i)
    return True

def try_with_omission(report, i):
    [first_report, second_report, third_report] = [report.copy(), report.copy(), report.copy()]
    
    first_report.pop(i - 1)
    second_report.pop(i)
    third_report.pop(i + 1)

    return report_safe(first_report, False) or report_safe(second_report, False) or report_safe(third_report, False)

def part_one(file):
    reports = parse_file(file)
    return sum([report_safe(report, False) for report in reports])

def part_two(file):
    reports = parse_file(file)
    return sum([report_safe(report, True) for report in reports])

if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))