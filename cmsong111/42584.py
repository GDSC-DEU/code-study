from collections import deque

def solution(prices):
    answer = []
    len_prices = len(prices)
    prices = deque(prices)

    while(prices):
        answer_temp = 0
        temp = prices.popleft()
        for i in prices:
            answer_temp+=1
            if temp > i:
                break


        answer.append(answer_temp)
        
    print("정답: ",answer)
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42584

prices = [1, 2, 3, 2, 3]
solution(prices)
#answer = [4, 3, 1, 1, 0]