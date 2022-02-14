def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = [0 for _ in range(bridge_length)]

    while bridge_queue:
        answer += 1
        bridge_queue.pop(0)
        if truck_weights:
            if sum(bridge_queue) + truck_weights[0] <= weight:
                bridge_queue.append(truck_weights.pop(0))
            else:
                bridge_queue.append(0)
    return answer