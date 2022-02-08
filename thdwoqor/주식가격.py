from collections import deque
def solution(prices):
    prices_queue=deque(prices)
    answer = [0]*len(prices)

    stack = []
    time=0
    now_prices=0
    while prices_queue:
        time+=1

        value=prices_queue.popleft()
        now_prices=value

        while len(stack)>0 and stack[-1][0]>now_prices:
            a,b = stack.pop()
            # print(a,b,time)
            answer[b-1]=time-b

        stack.append((value,time))

    while stack:
        a,b = stack.pop()
        answer[b-1]=time-b

    # print(time)


    return answer


prices=[1, 2, 3, 2, 3]

print(*solution(prices))