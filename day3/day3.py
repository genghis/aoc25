testdata = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
realdata = [x.strip() for x in open('data.txt')]

def part1(data):
    joltage = 0
    for i in data:
        first_digit = max(i[:-1])
        next_segment_start = i.index(first_digit)+1
        second_digit = max(i[next_segment_start::])
        joltage += int(first_digit+second_digit)
    return joltage

def i_guess_we_doin_recursion_now(segment, newjoltage):
    if len(segment) + len(newjoltage) == 12:
        return int(newjoltage+segment)
    boundary = len(segment)-(11-len(newjoltage))
    newjoltage += max(segment[:boundary])
    if len(newjoltage) == 12:
        return int(newjoltage)
    next_segment_start = segment.index(newjoltage[-1])+1
    nextsegment = segment[next_segment_start::]
    return i_guess_we_doin_recursion_now(nextsegment, newjoltage)
    
def part2(data):
    joltage = 0
    for i in data:
        joltage += i_guess_we_doin_recursion_now(i, '')
    return joltage

if __name__ == "__main__":
    print(f"Test 1: {part1(testdata)}")
    print(f"Part 1: {part1(realdata)}")
    print(f"Test 2: {part2(testdata)}")
    print(f"Part 2: {part2(realdata)}")