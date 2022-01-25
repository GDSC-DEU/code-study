def solution(progresses, speeds):
    queue = []
    day = 0

    for p, s in zip(progresses, speeds):
        d = 0
        while p < 100:
            p += s
            d += 1

        if d > day:
            day = d
            queue.append(1)
        else:
            queue[-1] += 1

    return queue