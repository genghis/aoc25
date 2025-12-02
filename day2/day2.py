testinput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
realinput = open("data.txt").read()

def make_data(inputvar):
    return inputvar.split(",")

def simple_dupe_check(numberstring):
    middle = int(len(numberstring)/2)
    if numberstring[:middle] == numberstring[middle:]:
        return int(numberstring)
    else:
        return 0

def complex_dupe_check(numberstring):
    middle = int(len(numberstring)/2)+1
    for i in range(1, middle):
        if len(numberstring) % i == 0:
            if numberstring.count(numberstring[:i]) == len(numberstring)/i:
                return int(numberstring)
    else:
        return 0
            

def part_one(data):
    invalid_total = 0
    cleanranges = [[str(y) for y in range(int(x.split("-")[0]), int(x.split("-")[1])+1 )] for x in data]
    for i in cleanranges:
        for j in i:
            if len(j) % 2 == 0:
                invalid_total += simple_dupe_check(j)
    return invalid_total

def part_two(data):
    invalid_total = 0
    cleanranges = [[str(y) for y in range(int(x.split("-")[0]), int(x.split("-")[1])+1 )] for x in data]
    for i in cleanranges:
        for j in i:
            digit_counts = {}
            for k in j:
                digit_counts[k] = j.count(k)
            if len(j) > 1 and len(digit_counts.keys()) == 1:
                invalid_total += int(j)
            elif all(value > 1 for value in digit_counts.values()):
                invalid_total += complex_dupe_check(j)
    return invalid_total

if __name__ == "__main__":
    print(f"Part1 Test: {part_one(make_data(testinput))}")
    print(f"Part1: {part_one(make_data(realinput))}")
    print(f"Part2 Test: {part_two(make_data(testinput))}")
    print(f"Part2: {part_two(make_data(realinput))}")