from itertools import permutations


def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    return True 

def solution(numbers):
    answer = 0
    lst = []
    p = []

    for i in range(1, len(numbers) + 1):
        lst = []
        lst.append(set(map(''.join, permutations(numbers, i))))
        for j in lst[0]:
            p.append(int(j))
    p = set(p)
    
    for i in p:
        if is_prime_num(i) == True:
            answer += 1
    
    return answer