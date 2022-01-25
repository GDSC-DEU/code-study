def solution(priorities, location):
    print_queue = []
    priority_queue = sorted(priorities, reverse=True)

    for i, p in enumerate(priorities):
        print_queue.append([i, p])

    priority = 1
    while len(print_queue) != 0:
        if print_queue[0][1] < priority_queue[0]:
            print_queue.append(print_queue.pop(0))
        else:
            if print_queue.pop(0)[0] == location:
                return priority
            priority_queue.pop(0)
            priority += 1