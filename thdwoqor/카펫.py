def solution(brown, yellow):
    answer = []

    for i in range(1, int(yellow / 2) + 2):
        for j in range(1, i + 1):
            if i * j > yellow:
                continue
            if i < j:
                continue
            wigth = i
            hight = j

            if wigth * 2 + (hight + 2) * 2 + wigth * hight == brown + yellow:
                answer.append(wigth + 2)
                answer.append(hight + 2)
                return answer
    return answer


brown = 8
yellow = 1
print(solution(brown, yellow))
