testinput = [x.split() for x in open("test.txt").readlines()]
realinput = [x.split() for x in open("data.txt").readlines()]
    
def part_one(data):
    grandtotal = 0
    for i in range(len(data[0])):
        if data[-1][i] == '*':
            grandtotal += int(data[0][i]) * int(data[1][i]) * int(data[2][i]) * int(data[3][i])
        else:
            grandtotal += int(data[0][i]) + int(data[1][i]) + int(data[2][i]) + int(data[3][i])
    return grandtotal

def part_two():
    total = 0
    segment_starts = []
    usable_data = open("data.txt").readlines()
    for idx, val in enumerate(usable_data[-1]):
        if val == '*' or val == '+':
            segment_starts.append(idx)
    problems = []
    for idx, col in enumerate(segment_starts[:-1:]):
        problems.append((usable_data[0][col:segment_starts[idx+1]-1],usable_data[1][col:segment_starts[idx+1]-1],usable_data[2][col:segment_starts[idx+1]-1],usable_data[3][col:segment_starts[idx+1]-1],usable_data[4][col]))
    problems.append((usable_data[0][segment_starts[-1]:-1],usable_data[1][segment_starts[-1]:-1],usable_data[2][segment_starts[-1]:-1],usable_data[3][segment_starts[-1]:-1],usable_data[-1][segment_starts[-1]]))
    for i in problems:
        length = len(i[0])
        numbers = []
        operator = i[-1]
        for j in range(length):
            number = ''
            for k in i[:-1]:
                if k[j].isnumeric():
                    number += k[j]
            numbers.append(int(number))
        if operator == '*':
            value = 1
            for i in numbers:
                value *= i
            total += value
        elif operator == '+':
            total += sum(numbers)
    return total
    
if __name__ == "__main__":
    # print(part2input)
    # print(f'Test 1: {part_one(testinput)}')
    # print(f'Part 1: {part_one(realinput)}')
    print(part_two())