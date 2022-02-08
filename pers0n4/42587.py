# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities: list[int], location: int):
    waiting_list = []
    priority_sequence = list(enumerate(priorities))

    while priority_sequence:
        index, priority = priority_sequence.pop(0)
        for _, candidate in priority_sequence:
            # 현재 작업의 우선 순위가 큐에 있는 작업의 우선 순위보다 낮은 경우
            if priority < candidate:
                priority_sequence.append((index, priority))
                break
        else:
            waiting_list.append(index)

    return waiting_list.index(location) + 1
