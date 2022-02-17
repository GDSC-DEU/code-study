def solution(citations):
    citations_len = len(citations)
    answer = []
    
    citations.sort()
    print(citations)

    for i in range(0,citations[citations_len-1]+1,1):
        print("H-index true?",i)
        tempup = 0
        tempdown = 0
        for ii in citations:
            if i < ii:
                tempup += 1
            elif i > ii:
                tempdown += 1
            else: #값이 같을때
                tempup += 1
                tempdown += 1
        
        if tempup >= i:
            if tempdown <= i:
                answer.append(i)
                print(tempup)
                print(tempdown)
        
        print("\n\n")

    print(answer)

    if answer:
        print("정답: ",max(answer))
        return max(answer)

    print("0")
    return 0



citations = [3, 0, 6, 1, 5]
solution(citations)

#citations =  [31, 66]
#solution(citations)