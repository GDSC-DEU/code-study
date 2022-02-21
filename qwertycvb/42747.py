def solution(citations):
    citations.sort(reverse = True)

    for idx, n in enumerate(citations):
        if idx >= n:
            return idx
    
    return len(citations)
