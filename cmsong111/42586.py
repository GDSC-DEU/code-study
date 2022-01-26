import math

def solution(progresses, speeds):
    count = len(speeds)
    answer = []
    result = []
    for i in range(count):
        answer.append(math.ceil((100 - progresses[i] )/ speeds[i]))
    print(answer)
    for i in range(1,count,1):
        if answer[i-1] > answer[i]:
            answer[i] = answer[i-1]
    print(answer)
    temp = {}
    for i in range(count):
        if answer[i] not in temp:
            temp[answer[i]] =1
        elif answer[i] in temp:
            temp[answer[i]] +=1
    print(temp)
    for value in temp:
        result.append(temp[value])    
    print(result)
    return result


# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# solution(progresses,speeds)
# answer = [2, 1]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
# solution(progresses,speeds)
# answer = [1, 3, 2]