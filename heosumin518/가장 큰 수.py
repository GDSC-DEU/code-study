numbers = [3, 30, 34, 5, 9, 121, 12]
answer = ''
l = []

for number in numbers:
    repeatNum = (str(number)*4)[:4]
    l.append((repeatNum, number))
    l.sort(reverse=True)
answer += "".join(str(i[1]) for i in l)

###### 시간 초과 발생 ######

# 프로그래머스 제출 코드
def solution(numbers):
    answer = ''
    l = []
    for number in numbers:
        repeatNum = (str(number)*4)[:4]
        l.append((repeatNum, number))
        l.sort(reverse=True)
    answer += "".join(str(i[1]) for i in l)
    return answer