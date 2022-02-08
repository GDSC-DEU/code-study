def solution(clothes):
    clothes_len = len(clothes)
    arr_dict = {}
    answer = 1
    print("-------------입력부--------------")
    for i in range(clothes_len):
        if clothes[i][1] not in arr_dict:
            arr_dict[clothes[i][1]] = 1
        else:
            arr_dict[clothes[i][1]] += 1
        
    arr_dict_len = len(arr_dict)
    print("딕셔너리",arr_dict)
    
    keyList = arr_dict.keys()
    print("키 리스트: ",keyList)

    print("-----------처리부----------------")

    for item in keyList :
        answer *= (arr_dict[item]+1)
        print(arr_dict[item])
        print("중간보고 answer: ",answer,"\n이 아이템을 정리함",item)
    answer -= 1
    print("------------결과 프린트---------------")

    #프린트 구문
    print(arr_dict)
    print("옷 가지 수", clothes_len)
    print("리스트 길이: ",arr_dict_len)
    print("정답: ",answer)

    return answer

#정답 5
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)

#정답 3
#clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
#solution(clothes)   