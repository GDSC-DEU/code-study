# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n: int, lost: list[int], reserve: list[int]):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

    return n - len(lost_set)
