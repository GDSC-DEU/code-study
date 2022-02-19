import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    print("입력확인:",scoville,"\n")
    while(len(scoville))!=1:
        temp = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        print("어떤거 작업하는지 확인용: ",temp,",",temp2)
        heapq.heappush(scoville,temp + (temp2 * 2))
        print("작업후 결과 확인: ",scoville)
        answer+=1

        temp = heapq.heappop(scoville)
        print("여기서 제일 작은 값은?: ",temp)
        if temp > K:
            heapq.heappush(scoville,temp)
            break
        heapq.heappush(scoville,temp)
        print()

    
    print(scoville)

    temp = heapq.heappop(scoville)
    if temp <= K:
        answer = -1
        
    print("\n정답:",answer)
    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville, K)
# answer = 2