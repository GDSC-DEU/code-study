def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    first_score = 0
    second = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    second_score = 0
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    third_score = 0
    max_score = 0
    for i, j in enumerate(answers):
        if first[i % len(first)] == j:
            first_score += 1
        if second[i % len(second)] == j:
            second_score += 1
        if third[i % len(third)] == j:
            third_score += 1

    max_score = max(first_score, second_score, third_score)
    for i, j in enumerate([first_score, second_score, third_score]):
        if j == max_score:
            answer.append(i + 1)
    return answer


answers = [1, 3, 2, 4, 2, 3]
print(solution(answers))
