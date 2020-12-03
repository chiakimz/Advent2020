
with open("3/input.txt") as f:
    context = f.readlines()
treeMap = [x.strip() for x in context]

def tobogganTrajectory():
    steps = 3
    trees = 0
    for road in range(1, len(treeMap)):
        r = treeMap[road]
        spot = treeMap[road][steps]
        if spot == "#":
            trees += 1
        if steps > 27:
            steps = steps - 28
        else:
            steps += 3
    return trees

print(tobogganTrajectory())

def tobogganTrajectory1():
    steps = 1
    trees1 = 0
    for road in range(1, len(treeMap)):
        r = treeMap[road]
        spot = treeMap[road][steps]
        if spot == "#":
            trees1 += 1
        if steps == 30:
            steps = 0
        else:
            steps += 1

    steps = 5
    trees2 = 0
    for road in range(1, len(treeMap)):
        r = treeMap[road]
        spot = treeMap[road][steps]
        if spot == "#":
            trees2 += 1
        if steps > 25:
            steps = steps - 26
        else:
            steps += 5

    steps = 7
    trees3 = 0
    for road in range(1, len(treeMap)):
        r = treeMap[road]
        spot = treeMap[road][steps]
        if spot == "#":
            trees3 += 1
        if steps > 23:
            steps = steps - 24
        else:
            steps += 7

    steps = 1
    trees4 = 0
    for road in range(1, len(treeMap)):
        if road % 2 == 0:
            r = treeMap[road]
            spot = treeMap[road][steps]
            if spot == "#":
                trees4 += 1
            if steps == 30:
                steps = 0
            else:
                steps += 1

    return tobogganTrajectory() * trees1 * trees2 * trees3 * trees4
print(tobogganTrajectory1())