# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers: list[int]):
    from itertools import cycle

    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    correct_answers = list(
        map(
            lambda pair: len(list(filter(lambda x: x[0] == x[1], pair))),
            map(lambda pattern: zip(answers, cycle(pattern)), patterns),
        )
    )
    return [
        i + 1
        for i, answer in enumerate(correct_answers)
        if answer == max(correct_answers)
    ]
