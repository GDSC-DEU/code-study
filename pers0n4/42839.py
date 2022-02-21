# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839
def solution(numbers: str):
    from itertools import permutations

    flat_map = lambda f, xs: (y for x in xs for y in f(x))
    unique_numbers = list(
        filter(
            lambda number: number >= 2,
            set(
                flat_map(
                    lambda i: list(
                        map(lambda p: int("".join(p)), permutations(numbers, i + 1))
                    ),
                    range(len(numbers)),
                )
            ),
        )
    )

    prime_map = dict({number: True for number in unique_numbers})
    for n in unique_numbers:
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                prime_map[n] = False
                break

    return list(prime_map.values()).count(True)
