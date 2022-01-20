def solution(participant, completion):
    participant=sorted(participant)
    completion=sorted(completion)
    completion.append(" ")
    anser = [i for i, j in zip(participant, completion) if i != j or j == " "]
    return anser[0]