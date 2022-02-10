from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights=deque(truck_weights)
    bridge=deque()
    bridge_weight=0
    
    # bridge_length 다리 길이
    # 트럭길이 1
    # 트럭은 1초에 1만큼 이동
    # Maybe 1차선
    
    while True:
        if len(bridge)==len(truck_weights)==0:
            break
        answer+=1
        if len(bridge)>0 and answer-bridge[0][0]==bridge_length:
            bridge_weight-=bridge.popleft()[1]
        if len(bridge)<=bridge_length: #브릿지 길이만큼 트럭 수용가능
            if truck_weights and truck_weights[0]+bridge_weight<=weight: #트럭이 없거나, 무게 초과일시 수용불가능
                truck_weights_value=truck_weights.popleft()
                
                bridge.append((answer,truck_weights_value))
                bridge_weight+=truck_weights_value

    return answer

# bridge_length=2
# weight=10
# truck_weights=[7,4,5,6]

bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))