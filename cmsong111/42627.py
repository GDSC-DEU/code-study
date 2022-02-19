import heapq

def solution(jobs):
    answer = 0
    time = []
    nowtime = 0
    worktime = 0

    heapq.heapify(jobs) #힙 으로 변경
    now_working = []
    after_working = [] #대기열
    finishedtable = [] #완료된 작업
    count = len(jobs)

    while(1):

        if jobs:
            if jobs[0][0] <= nowtime:
                temp = heapq.heappop(jobs)
                after_working.append(temp)
                after_working = sorted(after_working, key=lambda x: x[1])
        
        if after_working:
            if not now_working:
                temp = after_working.pop(0)
                now_working.append(temp)
                worktime=0


        if now_working:
            if now_working[0][1] <= worktime:
                temp = now_working.pop()
                finishedtable.append(temp)
                time.append(nowtime-temp[0])

                if not now_working:
                    if after_working:
                        temp = after_working.pop(0)
                        now_working.append(temp)
                        worktime = 0


        nowtime+=1
        worktime+=1
        

        if not now_working and not after_working and not jobs:
            print("\n\n\n\n작업을 완료했습니다!")
            break


 
        print()
        print("현재 시간:",nowtime,"ms")
        print("Jobs:",jobs)
        print("현재 작업중",now_working)
        print("대기열",after_working)
        print("완료 작업",finishedtable)
        print("현재 작업중인 시간",worktime)
        print("스코어 현황",time)        

        print("-------------------------------")

        
    print(time)
    answer = sum(time)//count
    print("정답: 평균",answer,"ms")
    return answer



# https://programmers.co.kr/learn/courses/30/lessons/42627

# jobs = [[0, 3], [1, 9], [2, 6]]	
# solution(jobs) #9

# jobs = [[1, 3], [2, 9], [3, 6]]	
# solution(jobs)

jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
solution(jobs) #72