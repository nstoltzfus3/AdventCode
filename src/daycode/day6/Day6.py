
def part2():
    file1 = open('../../../resources/day6.txt', 'r')

    currGroup = {'people' : 0}
    totalQuestions = 0
    for line in file1.readlines():


        if (line == "\n" or line == None):
            for k,v in currGroup.items():
                if (v == currGroup['people'] and len(k) == 1):
                    totalQuestions += 1
            currGroup = {'people' : 0}
        else:
            line = line.strip()
            currGroup['people'] += 1
            for let in line:
                if let not in currGroup:
                    currGroup[let] = 1
                else:
                    currGroup[let] += 1

    if len(currGroup) > 1:
        for k, v in currGroup.items():
            if (v == currGroup['people'] and len(k) == 1):
                totalQuestions += 1
    return totalQuestions

if __name__ == "__main__":
    print(part2())