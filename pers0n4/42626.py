# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
def solution(scoville: list[int], K: int):
    from heapq import heapify, heappop, heappush

    heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
        answer += 1
        if all(map(lambda s: s >= K, scoville)):
            return answer
    return -1
