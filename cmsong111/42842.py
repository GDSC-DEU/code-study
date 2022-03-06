def solution(brown, yellow):
    max = brown//2 + 2

    for i in range(max-3,2,-1):
        if (i-2) * (max-i-2) == yellow:
            return [i,max-i]  


brown = 10
yellow = 2	
print(solution(brown, yellow)) 
# answer = [4, 3]

brown = 8	
yellow = 1
print(solution(brown, yellow)) 
# answer = [3, 3]

brown = 24	
yellow = 24	
print(solution(brown, yellow))
# answer = [3, 3]
