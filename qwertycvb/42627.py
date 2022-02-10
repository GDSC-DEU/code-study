def solution(jobs):
    answer = 0
    div = len(jobs)
    time = 0

    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                jobs.pop(i)
                break

            if jobs[i] == jobs[-1]:
                time += 1

    return answer // div