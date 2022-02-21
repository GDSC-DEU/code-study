# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations: list[int]):
    for h in range(len(citations), 0, -1):
        more = list(filter(lambda c: c >= h, citations))
        if len(more) >= h:
            return h
    return 0
