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
    pass

def part_one(data):
    invalid_total = 0
    cleanranges = [[str(y) for y in range(int(x.split("-")[0]), int(x.split("-")[1])+1 )] for x in data]
    for i in cleanranges:
        for j in i:
            if len(j) % 2 == 0:
                invalid_total += simple_dupe_check(j)
    return invalid_total

def part_two(data):
    pass

if __name__ == "__main__":
    print(f"Part1 Test: {part_one(make_data(testinput))}")
    print(f"Part1: {part_one(make_data(realinput))}")