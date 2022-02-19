# 리스트를 사용하여 스택 구조로 데이터를 처리 LIFO
# 데이터 입력 : push -> append()
# 데이터 출력 : pop -> pop()

# 큐 역시 리스트를 사용. FIFO
# 데이터의 입력 : push -> append()
# 데이터의 출력 : get -> pop(0)
# 0을 넣어주면 0번째, 즉 가장 앞의 원소를 뽑아냄

# 테스트 케이스
progresses = [93, 30, 55]
speeds = [1, 30, 5]

answer = []

# 작업기간 저장
for i in range(len(progresses)):
    cntDate = 0
    while(True):
            if progresses[i] >= 100:
                break
            else:
                cntDate += 1
                progresses[i] += speeds[i]
    answer.append(cntDate)     

# 결과물 출력
for i in range(len(progresses)):
    answer

print(answer)
        
