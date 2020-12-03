def part1(right, down):
    file1 = open('../../../resources/day3.txt', 'r')

    rightInd = 0
    tree = 0
    downCount = 0
    for line in file1.readlines():
        if (downCount % down == 0):
            if line.strip()[rightInd % len(line.strip())] == '#':
                tree += 1
            rightInd += right
        downCount += 1

    return tree

def part2(file1):
    rightInc = [1, 3, 5, 7]
    rightInd = [0, 0, 0, 0]
    trees = [0, 0, 0, 0]
    weirdTree = 0
    weirdInc = 0
    skip = False
    for line in file1.readlines():
        for i in range(len(rightInd)):
            if line.strip()[rightInd[i] % len(line.strip())] == '#':
                trees[i] += 1
            rightInd[i] += rightInc[i]
        if not skip:
            if line.strip()[weirdInc % len(line.strip())] == '#':
                weirdTree += 1
            weirdInc += 1
        skip = not skip


    print(trees)
    print(weirdInc)

if __name__ == "__main__":
    prod = 1
    prod *= part1(1, 1)
    prod *= part1(3, 1)
    prod *= part1(5, 1)
    prod *= part1(7, 1)
    prod *= part1(1, 2)
    print(prod)




