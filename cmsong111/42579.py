def solution(genres, plays):

    playDic = {}            # {장르 : 총 재생 횟수}
    music_count_dict = {}   # {장르 : [(플레이 횟수, 고유번호)]}
    answer = []     
    count = len(plays)


    for i in range(count):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        music_count_dict[genres[i]] = music_count_dict.get(genres[i], []) + [(plays[i], i)]


    genreSort = sorted(playDic.items(), key = lambda x: x[1], reverse = True)


    for (genre, totalPlay) in genreSort:
        music_count_dict[genre] = sorted(music_count_dict[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in music_count_dict[genre][:2]]

    #Print Output
    print("------------결과 프린트---------------")
    print("playDic\n",playDic)
    print("\nmusic_count_dict \n",music_count_dict)
    print("\ngenreSort\n",genreSort)
    print("\nvalue 개수: ",count)
    print("\nanswer: ",answer)

    return answer




genres = ["classic", "pop", "classic", "classic", "pop"]
plays =[500, 600, 150, 800, 2500]
solution(genres, plays)
#answer = [4, 1, 3, 0]
