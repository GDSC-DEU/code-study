def solution(genres, plays):
    ans = []
    genres_dict = {}

    for i, play in enumerate(plays):
        genres_dict.setdefault(genres[i], [0, []])
        genres_dict[genres[i]][0] += play
        genres_dict[genres[i]][1].append((i, play))

    for _, sorted_genre in sorted(genres_dict.items(), key=lambda k: k[1][0], reverse=True):
        best_album = sorted(sorted_genre[1], key=lambda k: (k[1], -k[0]), reverse=True)[:2]
        ans += ([v[0] for v in best_album])

    return ans