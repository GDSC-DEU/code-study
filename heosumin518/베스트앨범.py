from collections import Counter

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

song = []
for l,w in zip(genres, plays):
    song.append([l, w])
print(song)

songKind = Counter([kind for kind, count in song])
print(songKind)
