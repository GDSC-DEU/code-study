from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses_queue=deque(progresses)
    speeds_queue=deque(speeds)
    day=0
    temp=0
    while progresses_queue:
        day+=1
        while progresses_queue:
            if progresses_queue[0]+speeds_queue[0]*day>=100:
                progresses_queue.popleft()
                speeds_queue.popleft()
                temp+=1
            else:
                break
        if temp>0:
            answer.append(temp)
            temp=0

    return answer

progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))