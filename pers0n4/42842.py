# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown: int, yellow: int):
    size = brown + yellow
    candidates = [
        [size // i, i] for i in range(3, int(size ** 0.5) + 1) if size % i == 0
    ]

    return next(
        filter(
            lambda candidate: (candidate[0] - 2) * (candidate[1] - 2) == yellow,
            candidates,
        )
    )
