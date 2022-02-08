from collections import deque
def solution(priorities, location):
    answer = 0
    printer=0
    priorities_queue=deque(priorities)
    while True:
        chk=True
        for i in priorities_queue:
            if i>priorities_queue[0]:
                chk=False

        if chk:
            priorities_queue.popleft()
            printer+=1
        else:
            priorities_queue.append(priorities_queue.popleft())

        if location==answer:
            if chk:
                break
            else:
                location=len(priorities_queue)-1
                answer=-1

        answer+=1
    return printer

priorities=[1, 1, 9, 1, 1, 1]
location=0
print(solution(priorities, location))
