def solution(n, lost, reserve):
    training = [1]*(n+1)   #초기 선언

    for i in lost:     #보유 여부 체크, 중요포인트 여분가저온 친구도 훔침 당할 수 있음
        training[i] -= 1
    for i in reserve:
        training[i] += 1
    print("작업전:",training[1:])

    for i in range(1,n):
        if training[i] == 0: #먼저 앞사람한테서 가져오기
            if training[i-1] == 2:
                training[i-1] -= 1
                training[i] += 1
        if training[i] == 0: #뒷사람한테 빌려오기
            if training[i+1] == 2:
                training[i+1] -= 1
                training[i] += 1

    training[0] = 0
    print("작업후:",training[1:])


    training.sort(reverse=True)
    answer = training.index(0)
    print("정답:",answer,"\n")
    return answer


#https://programmers.co.kr/learn/courses/30/lessons/42862

n = 5	
lost = [2, 4]	
reserve = [1, 3, 5]	
solution(n, lost, reserve) #5

n = 5	
lost = [2, 4]	
reserve = [3]	
solution(n, lost, reserve) #4

n = 3	
lost = [3]	
reserve = [1]	
solution(n, lost, reserve) #2
