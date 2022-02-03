def solution(bridge_length, weight, truck_weights):
    answer = 0 
    now_bridge_weights = [0]*bridge_length
    #상황을 보기 위해서 넣은 리스트 clear_car임 제출시 삭제
    clear_car = []
    while(now_bridge_weights):
        temp = now_bridge_weights.pop(0)
        #제출시 아래 if 절삭제
        if temp != 0: 
            clear_car.append(temp)

        if truck_weights:
            if sum(now_bridge_weights)+truck_weights[0] <= weight:
                if truck_weights:
                    now_bridge_weights.append(truck_weights.pop(0))
            else:
                now_bridge_weights.append(0)
        answer += 1

        print("지나간 자동차",clear_car)
        print("현재 다리 상태: ",now_bridge_weights)
        print("현재 다리 무게",sum(now_bridge_weights))
        print("대기열: ",truck_weights)
        print("현재 시간:",answer,"초")
        print()
        
    
    print("정답:",answer)
    return answer


#https://programmers.co.kr/learn/courses/30/lessons/42583

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)
#answer = 8
print("-----------------------")

bridge_length = 100
weight = 100
truck_weights = [10]
solution(bridge_length, weight, truck_weights)
#answer = 101
print("-----------------------")

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)
#answer = 101
print("-----------------------")

#제출할떄는 print문, clear_car 관련 구문 제거하기
