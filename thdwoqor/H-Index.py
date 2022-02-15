def solution(citations: list):
    answer = []
    citations.sort()
    M = 0
    for i in range(10001):
        count = 0
        for j in citations:
            if j >= i:
                count += 1
        if count >= i:
            M = i
    return M


citations = [0, 0, 0, 0, 1]

print(solution(citations))
