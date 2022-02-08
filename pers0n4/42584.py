# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices: list[int]):
    answer = [0] * len(prices)
    for i, past in enumerate(prices):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            # 현재 가격이 이전 가격보다 낮아진 경우
            if past > prices[j]:
                break
    return answer
