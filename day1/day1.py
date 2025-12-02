testdata = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
realdata = [i.strip() for i in open("data.txt")]

def puzzle_one(dial_location, data, dial):
    count = 0
    for i in data:
        match i[0]:
            case "L":
                new_index = dial_location - int(i[1::])
            case "R":
                new_index = dial_location + int(i[1::])
        dial_location = new_index % dial
        if dial_location == 0:
            count += 1
    return count

def puzzle_two(dial_location, data, dial):
    count = 0
    for i in data:
        stringdigits = i[1::]
        if len(stringdigits) > 2:
            count += int(stringdigits[:-2])
        digits = int(stringdigits[-2:])

        match i[0]:
            case "L":
                new_index = dial_location - digits
                if dial_location != 0 and new_index <= 0:
                    count += 1
            case "R":
                new_index = dial_location + digits
                if new_index > 99:
                    count += 1
        dial_location = new_index % dial
    return count

if __name__ == "__main__":
    print(f"Test1 =", puzzle_one(50, testdata, 100))
    print(f"Test2 =", puzzle_two(50, testdata, 100))
    print(f"1.1 =", puzzle_one(50, realdata, 100))
    print(f"1.2 =", puzzle_two(50, realdata, 100))