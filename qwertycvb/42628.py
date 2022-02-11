from collections import deque


def solution(operations):
    dq = deque()

    for operation in operations:
        command, arg = operation.split()

        if command == "I":
            dq.insert(0, int(arg))
            dq = deque(sorted(dq))
        elif command == "D":
            if len(dq):
                if arg == "1":
                    dq.pop()
                else:
                    dq.popleft()
    if len(dq):
        return [dq.pop(), dq.popleft()]
    else:
        return [0, 0]
