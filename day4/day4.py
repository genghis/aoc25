testdata = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."
]

realdata = [str(x) for x in open("data.txt").readlines()]

def process_map(data):
    newdata = []
    for i in data:
        newdata.append("."+i+".")
    bufferline = "."*len(newdata[0])
    newdata.append(bufferline)
    newdata.insert(0, bufferline)
    return newdata

def check_surroundings(coords, grid):
    rolls = []
    x,y = coords
    rolls.append(grid[y-1][x-1])
    rolls.append(grid[y][x-1])
    rolls.append(grid[y+1][x-1])
    rolls.append(grid[y+1][x])
    rolls.append(grid[y+1][x+1])
    rolls.append(grid[y][x+1])
    rolls.append(grid[y-1][x+1])
    rolls.append(grid[y-1][x])
    if rolls.count("@") < 4:
        return 1
    else:
        return 0

def part_one(grid):
    accessible_rolls = 0
    for y,row in enumerate(grid):
        for x,char in enumerate(row):
            if char == "@":
                accessible_rolls += check_surroundings((x,y), grid)
    return accessible_rolls

def part_two(grid, accessible_rolls):
    newgrid = []
    for y,row in enumerate(grid):
        newrow = ""
        for x,char in enumerate(row):
            if char == "@":
                if check_surroundings((x,y), grid):
                    accessible_rolls += 1
                    newrow += "."
                else:
                    newrow += "@"
            else:
                newrow += "."
        newgrid.append(newrow)
    if grid == newgrid:
        return accessible_rolls
    else:
        return part_two(newgrid, accessible_rolls)

if __name__ == "__main__":
    testgrid = process_map(testdata)
    realgrid = process_map(realdata)
    print(f"Test 1: {part_one(testgrid)}")
    print(f"Part 1: {part_one(realgrid)}")
    print(f"Test 2: {part_two(testgrid, 0)}")
    print(f"Part 2: {part_two(realgrid, 0)}")