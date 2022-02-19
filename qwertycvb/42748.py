def solution(array, commands):
    answer = []
    for command in commands:
        c1, c2, c3 = command
        answer.append(list(sorted(array[c1-1:c2]))[c3-1])
    return answer
