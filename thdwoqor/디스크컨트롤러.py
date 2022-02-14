import heapq
import math
def solution(jobs:list):
    answer = 0
    denominator=len(jobs)
    heap=[]
    heapq.heapify(jobs)
    now=0
    
    # for i,j in jobs:
    #     heapq.heappush(job, (j,i))
    
    while True:
        if len(jobs)==0 and len(heap)==0:
            break
        while True:
            if len(jobs)>0 and jobs[0][0]<=now:
                i,j=heapq.heappop(jobs)
                heapq.heappush(heap, (j,i))
            else:
                break
        # print(jobs,'/',heap)
        if len(heap)>0:
            # while heap:
            j,i=heapq.heappop(heap)
            answer+=j+now-i
            now+=j
        else:
            now+=1

    answer=math.trunc(answer/denominator)
    # answer=answer//denominator
    return answer

#9
# jobs=[[0, 3], [1, 9], [2, 6]]
#72
# jobs=[[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
#15
jobs=[[0, 10], [4, 10], [15, 2], [5, 11]]
#6
# jobs=[[0, 5], [2, 10], [10000, 2]]
print(solution(jobs))