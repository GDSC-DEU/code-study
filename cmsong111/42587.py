from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])
    print(d)

    while len(d):
        item = d.popleft()
        print(item,d)
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
 
    print(answer)
    return answer

priorities = [2, 1, 3, 2]
location = 	2
solution(priorities,location)
# answer = 1

priorities = [1, 1, 9, 1, 1, 1]
location = 	1
solution(priorities,location)
# answer = 5
