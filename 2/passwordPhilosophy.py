import re
with open("2/input.txt") as f:
    context = f.readlines()
    content = []
    for line in context:
        line = re.sub(r'[^\w]', ' ', line)
        content.append(line.replace('  ', ' ').split(' ')[:4])

def passwordPhilosophy():
    valid = 0
    for line in content:
        min = int(line[0])
        max = int(line[1])
        letter = line[2]
        password = line[3]
        occurence = password.count(letter)
        if min <= occurence and occurence <= max:
            valid += 1
    return valid

def passwordPhilosophy1():
    valid = 0
    for line in content:
        first = int(line[0]) - 1
        second = int(line[1]) - 1
        letter = line[2]
        password = line[3]
        if password[first] == letter and password[second] != letter or password[first] != letter and password[second] == letter:
            valid += 1
    return valid


print(passwordPhilosophy())
print(passwordPhilosophy1())