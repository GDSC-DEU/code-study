# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes: list[list[str]]):
    from functools import reduce

    hash_table: dict[str, int] = {}
    # 옷 종류별 카운트
    for _, category in clothes:
        hash_table.setdefault(category, 1)
        hash_table[category] += 1

    return reduce(lambda x, y: x * y, hash_table.values()) - 1
