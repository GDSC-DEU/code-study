# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses: list[int], speeds: list[int]):
    from math import ceil

    # 남은 진행도 계산
    remains_progresses = map(lambda progress: 100 - progress, progresses)
    remains_day = [
        ceil(remains_progress / speed)
        for remains_progress, speed in zip(remains_progresses, speeds)
    ]

    batch = []
    while remains_day:
        remain = remains_day.pop(0)
        count = 1
        # 다음 작업의 남은 일수가 현재 남은 일수보다 같거나 작은 경우
        while remains_day and remain >= remains_day[0]:
            remains_day.pop(0)
            count += 1
        batch.append(count)

    return batch
