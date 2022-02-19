import heapq

K = 7   # 스코빌 지수
scoville = [1, 2, 3, 9, 10, 12]     # Leo가 가진 음식의 스코빌 지수를 담은 배열
scoville_food = []      # 스코빌 음식을 힙 정렬 방식으로 담을 새로운 배열
mixed_food = 0     # 섞은 음식의 스코빌 지수
count = 0       # 음식을 섞은 횟수

# 모든 원소를 차례대로 힙에 삽입 (꺼낼 때의 시간복잡도를 위해 힙에 재삽입하는 과정)
for value in scoville:
    heapq.heappush(scoville_food, value)

while(True):

    # 모든 음식의 스코빌 지수가 K 이상이면 섞은 횟수를 출력하고 프로그램을 종료한다.
    if scoville_food[0] >= K:
        print(count)
        break
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 리턴
    if len(scoville_food) == 1:
        if scoville_food[0] <= K:
            print(-1)
            break

    # 특별한 방법으로 두 음식을 섞어 스코빌 지수를 올린 새 음식을 만듦
    mixed_food = heapq.heappop(scoville_food) + (heapq.heappop(scoville_food) * 2)

    count += 1      # 음식 섞은 횟수 추가

    # 새로 만들어진 음식을 음식 리스트에 다시 집어넣음
    heapq.heappush(scoville_food, mixed_food)
