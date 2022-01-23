def solution(clothes):
    clothes_len = len(clothes)
    arr_dict = {}

    for i in range(clothes_len):
        if clothes[i][1] not in arr_dict:
            arr_dict[clothes[i][1]] = 1
        else:
            arr_dict[clothes[i][1]] += 1
        
    arr_dict_len = len(arr_dict)
    print(arr_dict)
    answer = 1

    keyList = arr_dict.keys()
    for i in range(arr_dict_len):
        for item in keyList :
            answer *= (arr_dict[item]+1)
            
    answer -=1
    return answer

