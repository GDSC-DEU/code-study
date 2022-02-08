# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length: int, weight: int, truck_weights: list[int]):
    answer = 0
    index = 0
    bridge = [0] * bridge_length
    while truck_weights:
        bridge[index] = 0
        # 현재 다리에 있는 트럭의 총 무게와 다음 트럭의 무게가 다리의 무게를 초과하지 않는 경우
        if sum(bridge) + truck_weights[0] <= weight:
            bridge[index] = truck_weights.pop(0)
        answer += 1
        index = answer % bridge_length
    return answer + bridge_length
