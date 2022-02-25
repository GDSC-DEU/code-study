def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]
    ans = []
    
    for i, answer in enumerate(answers):
        if s1[i % len(s1)] == answer:
            scores[0] += 1
        if s2[i % len(s2)] == answer:
            scores[1] += 1
        if s3[i % len(s3)] == answer:
            scores[2] += 1

    for i, score in enumerate(scores):
        if score == max(scores):
            ans.append(i + 1)
    return ans
