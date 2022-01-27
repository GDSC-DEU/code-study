def solution(clothes):
    ans = 1
    cloth_dict = {}

    for _, t in clothes:
        cloth_dict.setdefault(t, 1)
        cloth_dict[t] += 1

    for i in cloth_dict.values():
        ans *= i

    return ans - 1
