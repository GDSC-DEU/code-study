# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres: list[str], plays: list[int]):
    genre_table: dict[str, list[tuple[int, int]]] = {}
    # 장르를 기준으로 노래 매핑
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_table.setdefault(genre, [])
        genre_table[genre].append((index, play))

    # 인기 장르 순 정렬
    best_genres = sorted(
        genre_table,
        key=lambda genre: sum(map(lambda song: song[1], genre_table[genre])),
        reverse=True,
    )
    # 장르 내 인기 노래 순 정렬
    best_albums = map(
        lambda genre: map(
            lambda song: song[0],
            sorted(genre_table[genre], key=lambda song: song[1], reverse=True)[:2],
        ),
        best_genres,
    )

    return [song for genre in best_albums for song in genre]
