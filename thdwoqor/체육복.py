def solution(n: int, lost: list, reserve: list) -> int:
    answer = 0
    lost.sort()
    reserve.sort()

    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    for i in reserve:
        if i - 1 in lost[:]:
            lost.remove(i - 1)
            continue
        if i + 1 in lost[:]:
            lost.remove(i + 1)
    answer = n - len(lost)
    return answer


# n = 5
# lost = [2, 4]
# reserve = [3]
print(solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9]))
