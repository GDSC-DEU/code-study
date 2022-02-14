import heapq


def solution(operations: list):
    answer_max = []
    count_max = 0
    answer_min = []
    count_min = 0
    for i in operations:
        word, num = i.split()
        num = int(num)

        if word == "I":
            heapq.heappush(answer_max, -num)
            heapq.heappush(answer_min, num)
        elif word == "D" and num == -1:

            if len(answer_min) - count_min > 0:
                heapq.heappop(answer_min)
                count_max += 1
            if len(answer_min) - count_min == 0:
                answer_min = []
                count_min = 0
        elif word == "D" and num == 1:

            if len(answer_max) - count_max > 0:
                heapq.heappop(answer_max)
                count_min += 1
            if len(answer_max) - count_max == 0:
                answer_max = []
                count_max = 0

    a, b = 0, 0

    if len(answer_max) - count_max > 0:
        a = -heapq.heappop(answer_max)
    if len(answer_min) - count_min > 0:
        b = heapq.heappop(answer_min)
    return [a, b]


# ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"] [6,5]
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
print(solution(operations))
