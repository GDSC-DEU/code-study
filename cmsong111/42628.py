def solution(operations):
    answer = []
    arr = []
    for i in operations:
        a,b = i.split()
        b = int(b)
        if a == "I":
            arr.append(b)
        if a == "D":
            if arr:
                if b == 1:
                    arr.remove(max(arr))
                if b == -1:
                    arr.remove(min(arr))


    if arr:
        answer.append(max(arr))
        answer.append(min(arr))
    else:
        answer = [0,0]

    return answer


#https://programmers.co.kr/learn/courses/30/lessons/42628

operations = ["I 16","D 1"]
solution(operations)
print()
operations= ["I 7","I 5","I -5","D -1"]
solution(operations)