import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while len(scoville)>1:
        if scoville[0]>=K:
            return count
        count+=1
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
    if len(scoville)==1 and scoville[0]>=K:
        return count
    return -1
    

scoville=[1, 2, 3, 9, 10, 12]
K=7

solution(scoville, K)