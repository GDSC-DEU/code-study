# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.
# 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return

operations = 	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

answer = []
myQue = []

# myQue.append("18")

# myQue.sort()
# # duoQue.sort(reverse=True)

for i in operations:
    num1, num2 = i.split()
    if num1 == "I":     # 큐에 주어진 숫자 삽입
        myQue.append(int(num2))
        myQue.sort()    # 오름차순 정렬

    elif num1 == "D":       # 큐에서 숫자 삭제
        if not myQue:   
            pass
        elif num2 == "1":    # 최댓값 삭제
            del myQue[len(myQue)-1]
        elif num2 == "-1":     # 최솟값 삭제
            del myQue[0]

if len(myQue) == 0:     # 큐가 비어있을 때
    answer = [0, 0]
else:
    answer.append(int(myQue[len(myQue)-1]))  # 최댓값 삽입
    answer.append(int(myQue[0]))     # 최솟값 삽입







# 프로그래머스 제출 코드
def solution(operations):
    answer = []
    myQue = []
    for i in operations:
        num1, num2 = i.split()
        if num1 == "I":     # 큐에 주어진 숫자 삽입
            myQue.append(int(num2))
            myQue.sort()    # 오름차순 정렬

        elif num1 == "D":       # 큐에서 숫자 삭제
            if not myQue:   
                pass
            elif num2 == "1":    # 최댓값 삭제
                del myQue[len(myQue)-1]
            elif num2 == "-1":     # 최솟값 삭제
                del myQue[0]

    if len(myQue) == 0:     # 큐가 비어있을 때
        answer = [0, 0]
    else:
        answer.append(int(myQue[len(myQue)-1]))  # 최댓값 삽입
        answer.append(int(myQue[0]))     # 최솟값 삽입

    return answer