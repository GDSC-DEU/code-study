array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

sliced = []     # 슬라이싱한 배열을 담을 배열
answer = []     # k번째 숫자들을 담을 배열

for i in commands:
    print(i) 
    sliced = array[i[0]-1:i[1]]
    sliced.sort()
    answer.append(sliced[i[2]-1])

#######구현 완료#######

# 프로그래머스 제출 코드
def solution(array, commands):
    sliced = []
    answer = []
    for i in commands:
        print(i) 
        sliced = array[i[0]-1:i[1]]
        sliced.sort()
        answer.append(sliced[i[2]-1])
    return answer