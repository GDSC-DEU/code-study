# import itertools


# def solution(numbers: list):
#     answer = 0
#     nPr = itertools.permutations(numbers, len(numbers))
#     for i in nPr:
#         number = ""
#         for j in i:
#             number += str(j)
#         answer = max(answer, int(number))
#     return str(answer)


# numbers = [3, 30, 34, 5, 9]

# print(solution(numbers))


def solution(numbers: list):
    answer = []
    merge = ""
    for number in numbers:
        if number == 1000:
            answer.append(("1000", number))
        else:

            answer.append(((str(number) * 6)[:6], number))
    answer.sort(key=lambda x: (-int(x[0]), x[1]))

    for i in answer:
        merge += str(i[1])
    if int(merge) == 0:
        merge = "0"
    return merge


# numbers = [979, 97, 978, 81, 818, 817]
numbers = [
    67,
    676,
    677,
]
# numbers = [6, 10, 2]
print(solution(numbers))
