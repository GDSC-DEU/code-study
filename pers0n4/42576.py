# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant: list[str], completion: list[str]):
    players: dict[str, int] = {}

    # 참가자 테이블 생성
    for p in participant:
        players[p] = players.get(p, 0) + 1

    # 완주자 목록에 있는 참가자 제거
    for c in completion:
        players[c] -= 1

    return list(filter(lambda p: p[1] != 0, players.items())).pop()[0]
