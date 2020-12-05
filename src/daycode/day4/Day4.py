from pprint import pprint as pp

def part1():
    file1 = open('../../../resources/day4.txt', 'r')

    hitCreds = 0

    curPass = {}
    validPassports = 0
    for line in file1.readlines():

        if (line == "\n"):
            if len(curPass) >= 8:
                validPassports += 1
            elif (len(curPass) == 7 and 'cid' not in curPass):
                validPassports += 1
            curPass = {}
            continue
        parts = line.split()
        passSections = [x.split(':') for x in parts]
        for i in range(len(passSections)):
            curPass[passSections[i][0]] = passSections[i][1]
    return validPassports

def evalIssueYear(year):
    year = int(year)
    return year <= 2020 and year >= 2010

def evalBirthYear(year):
    year = int(year)
    return year <= 2002 and year >= 1920

def evalExpYear(year):
    year = int(year)
    print(year)
    return year >= 2020 and year <= 2030

def evalHeight(height):
    measure = height[:-2]
    dataT = height[-2:]
    if ("cm" in dataT):
        return int(measure) >= 150 and int(measure) <= 193
    elif ("in" in dataT):
        return int(measure) >= 59 and int(measure) <= 76
    else:
        return False

def evalHair(color):
    chars = "1234567890abcdef"
    if (len(color) != 7 or color[0] != '#'):
        return False
    for let in color[1:]:
        if let not in chars:
            return False
    return True

def evalEyes(colorStr):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if colorStr not in colors:
        return False
    else:
        return True

def evalPID(number):
    nums = "1234567890"
    for i in number:
        if i not in nums:
            return False
    if len(number) > 9:
        return False
    elif len(number) == 9:
        return True
    else:
        return False

def evalPassPort(curPass):
    return (evalBirthYear(curPass["byr"]) and
                        evalIssueYear(curPass["iyr"]) and
                        evalHeight(curPass["hgt"]) and
                        evalExpYear(curPass["eyr"]) and
                        evalEyes(curPass["ecl"]) and
                        evalHair(curPass["hcl"]) and
                        evalPID(curPass["pid"]))

def part2():
    file1 = open('../../../resources/day4.txt', 'r')

    hitCreds = 0

    curPass = {}
    validPassports = 0
    total = 0
    for line in file1.readlines():

        if (line == "\n" or line == None):
            total += 1
            if len(curPass) < 7:
                curPass = {}
                continue
            elif ("byr" in curPass and
            "iyr" in curPass and
            "hgt" in curPass and
            "eyr" in curPass and
            "ecl" in curPass and
            "hcl" in curPass and
            "pid" in curPass):
                if (evalPassPort(curPass)):
                    print("valid!")
                    validPassports += 1
                else:
                    print("Invalid")
            else:
                print("Invalid")
            curPass = {}
            continue
        parts = line.split()
        passSections = [x.split(':') for x in parts]
        for i in range(len(passSections)):
            curPass[passSections[i][0]] = passSections[i][1]
    print(total)
    return validPassports


if __name__ == "__main__":
    # print(part1())
    print(part2())