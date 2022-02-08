# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book: list[str]):
    hash_table = dict(map(lambda x: (x, True), phone_book))
    for phone in phone_book:
        key = ""
        # phone의 서브 스트링이 해시에 있는지 확인
        for number in phone[:-1]:
            key += number
            if hash_table.get(key, False):
                return False
    return True
