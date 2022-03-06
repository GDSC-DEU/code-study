from itertools import permutations


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers: str):
    answer = 0
    for i in range(1, len(numbers) + 1):
        for j in set(list(permutations(list(numbers), i))):
            num = "".join(j)
            if num[0] == "0" or num == "1":
                continue
            if is_prime_number(int(num)):
                answer += 1
                # print(num)
    return answer


numbers = "011"
print(solution(numbers))
