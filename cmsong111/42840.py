def solution(answers):
    scores = [0,0,0]
    answer = []
    count = len(answers)

    s1 = [1,2,3,4,5]*(count//5+1)  #5
    s2 = [2,1,2,3,2,4,2,5]*(count//8+1) #8 
    s3 = [3,3,1,1,2,2,4,4,5,5]*(count//10+1) #10
    
    
    for i in range(count): 
        if answers[i] == s1[i]:
            scores[0] +=1
        if answers[i] == s2[i]:
            scores[1] +=1
        if answers[i] == s3[i]:
            scores[2] +=1
    max_score = max(scores)

    print("학생들 점수는: ",scores)

    for i in range(3):
        if max_score == scores[i]:
            answer.append(i+1)

    print("정답: ",answer)
    return answer


#https://programmers.co.kr/learn/courses/30/lessons/42840

answers = [1,2,3,4,5]
solution(answers)

print()

answers = [1,3,2,4,2]
solution(answers)