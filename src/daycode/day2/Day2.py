

def part1(min, max, password, letter):
    validCount = 0
    chars = {}
    for let in password:
        if not let in chars:
            chars[let] = 1
        else:
            chars[let] = chars[let] + 1

    if (letter in chars):
        if (chars[letter] >= min and chars[letter] <= max):
            validCount += 1
    elif (min == 0):
        validCount += 1

    return validCount


def part2(min, max, password, letter):
    validCount = 0
    contains = 0
    for i in [min, max]:
        if (password[min-1] == letter):
            contains += 1
        if (password[max-1] == letter):
            contains += 1
        validCount = validCount + 1 if contains == 1 else validCount


    return validCount


if __name__ == "__main__":
    file1 = open('../../../resources/day2.txt', 'r')
    validCount1 = 0
    validCount2 = 0
    for line in file1.readlines():

        # line parsing
        dash = line.find('-')
        min = int(line[:dash])
        space = line.find(' ', dash)
        max = int(line[dash+1:space])
        letter = line[space+1:space+2]
        space = line.find(' ', space+1)
        password = line[space+1:]
        password = password.strip()

        validCount1 += part1(min, max, password, letter)
        validCount2 += part2(min, max, password, letter)
    print(validCount1)
    print(validCount2)


