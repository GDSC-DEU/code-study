from itertools import permutations

#소수 판별 함수
def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    return True 

#메인 함수
def solution(numbers):
    answer = 0
    num_arr = []
    list_arr = []

    for count in range(1,len(numbers)+1):
        for i in list(permutations(numbers,count)):
            temp = ""
            for ii in i:
                temp += ii
            if int(temp) not in list_arr: 
                list_arr.append(int(temp))
    
    print(list_arr)

    for i in list_arr:
        if is_prime_num(i):
            answer+=1

    print(answer)
    return answer


#https://programmers.co.kr/learn/courses/30/lessons/42839

numbers = "17"
solution(numbers)
print()
numbers = "011"
solution(numbers)


