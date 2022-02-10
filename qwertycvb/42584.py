from collections import deque


def solution(prices):
    answer = []
    prices_queue = deque(prices)

    while prices_queue:
        time = 0
        price = prices_queue.popleft()
        for i in prices_queue:
            time += 1
            if price > i:
                break
        answer.append(time)
    return answer