
import time

with open("input.txt") as f:
    context = f.readlines()
content = [int(x.strip()) for x in context]

def findTwentyTwenty_twoNums():
    content.sort()
    index = -1
    for i in range(len(content)):
        while (content[i] + content[index]) > 2020:
            index -= 1
        if content[i] + content[index] == 2020:
            print(content[i], content[index])
            return content[i] * content[index]

answer = findTwentyTwenty_twoNums()
print(answer)

def findTwentyTwenty_threeNums():
    start_time = time.time()
    content.sort()
    for i in range(len(content)):
        index = -1
        for j in range(i + 1, len(content) + index):
            while (content[i] + content[j] + content[index]) > 2020:
                current = content[i] + content[j] + content[index]
                index -= 1
                if index == -201:
                    break
            if index == -201:
                break
            if content[i] + content[j] + content[index] == 2020:
                print(content[i], content[j], content[index])
                end_time = time.time()
                return content[i] * content[j] * content[index], end_time - start_time

answer, time_took = findTwentyTwenty_threeNums()
print(f"Answer: {answer}, First function time: {time_took}")

def findTwentyTwenty_threeNums1():
    start_time1 = time.time()
    content.sort()

    for i in range(len(content)):
        for j in range(i + 1, len(content)):
            for s in range(i + 2, len(content)):
                if (content[i] + content[j] + content[s]) > 2020:
                        break
                if content[i] + content[j] + content[s] == 2020:
                    print(content[i], content[j], content[s])
                    end_time1 = time.time()
                    return content[i] * content[j] * content[s], end_time1 - start_time1

answer1, time_took1 = findTwentyTwenty_threeNums1()
print(f"Answer: {answer1}, Second function time:{time_took1}")

