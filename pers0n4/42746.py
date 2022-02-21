# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers: list[int]):
    return "".join(sorted(map(str, numbers), key=lambda x: x * 3, reverse=True))
