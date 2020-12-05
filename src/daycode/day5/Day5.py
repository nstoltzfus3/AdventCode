def letToBin(big, string):
    return sum([(2**(len(string)-i-1) if string[i] == big else 0) for i in range(len(string))])

def part1():
    file1 = open('../../../resources/day5.txt', 'r')
    seatIDs = []

    for line in file1.readlines():
        line = line.strip()
        row = line[:-3]
        column = line[-3:]
        rowNum = letToBin('B', row)
        columnNum = letToBin('R', column)
        seatID = rowNum * 8 + columnNum
        seatIDs.append(seatID)

    return seatIDs

def part2(seatIDs):
    seatIDs.sort()
    for i in range(1, len(seatIDs)):
        if seatIDs[i] - seatIDs[i-1] > 1:
            print(seatIDs[i])
            print(seatIDs[i-1])

if __name__ == "__main__":
    print(max(part1()))
    print(part2(part1()))