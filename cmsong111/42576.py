#1 try
def solution(participant, completion):
    completion_len = len(completion)
    
    for i in range(completion_len):
        if completion[i] in participant:
            temp = participant.index(completion[i])
            participant.pop(temp)
    
    answer = participant[0]
        
    return answer



#2 try
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = participant.pop()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i] 
            break
   
    return answer

