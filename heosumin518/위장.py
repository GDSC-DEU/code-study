from collections import Counter

# 결과값
result = 1
#옷 종류별 갯수 확인
clothesKind = Counter([kind for name, kind in clothes])
for i in clothesKind.values():
    result *= (i+1)     # nCr * nCr * ...
# 아무것도 입지 않는 경우 제외
print(result-1)
