def solution(numbers):
    answer = ''
    
    #모든 리스트의 합이 0이면 0으로 출력 ex[0,0,0] -> 0
    if sum(numbers) == 0:
        return "0"
    
    count = len(numbers)

    result = []
    #리스트를 문자열로 변경
    for i in range(count):
        result.append(str(numbers[i]))
    print(result)

    #*5를 해줌으로써 문자열 기준으로 정렬시킴
    result.sort(key = lambda x: x * 5, reverse=True)
    
    print(result)
    
    #결과값을 문자열로 다 붙임
    for i in result:
        answer += i

    print(answer)
    return answer
    

numbers = [6, 10, 2]
solution(numbers)

numbers = [3, 30, 34, 5, 9]	
solution(numbers)

