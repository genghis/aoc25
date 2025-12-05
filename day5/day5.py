testinput = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
realinput = open("data.txt").read()

def parse_data(data):
    ranges,ids = data.split("\n\n")
    return (ranges, ids)

def part_one(data):
    count = 0
    ranges = data[0].split('\n')
    ids = data[1].split('\n')
    for i in ids:
        for j in ranges:
            beginning, end = j.split("-")
            if int(beginning) < int(i) < int(end):
                count += 1
                break
    return count

def part_two(data):
    count = 0
    ranges = [(int(x[0]), int(x[1])) for x in (x.split('-') for x in data[0].split('\n'))]
    sorted_ranges = sorted(ranges, key=lambda rng: rng[0])
    highest_number = 0
    for val in sorted_ranges:
        if val[0] > highest_number:
            count += val[1] - val[0] + 1
            highest_number = val[1]
        elif val[0] <= highest_number and val[1] > highest_number:
            count += val[1] - highest_number
            highest_number = val[1]
    return count

if __name__ == "__main__":
    print(f"Test 1: {part_one(parse_data(testinput))}")
    print(f"Part 1: {part_one(parse_data(realinput))}")
    print(f"Test 2: {part_two(parse_data(testinput))}")
    print(f"Part 1: {part_two(parse_data(realinput))}")