#include <string>
#include <vector>
#include<queue>
#include<iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0, count = 0;
	int sum = 0; //다리위에 있는 트럭 무게의 총 합
	queue<int> q;
	while (1) {

		//cout << count << ":" << truck_weights.size() << " ";

		if (count > truck_weights.size() - 1) //모든 트럭이 다 다리위에 올라갔을 때 
			break;
        //다리위에 있는 트럭의 무게의 총 합과 그 다음 기다리고 있는 트럭의 무게가 제한 무게보다 작은 경우
		if (sum + truck_weights[count] <= weight) { 
			if (q.size() < bridge_length) { //다리길이와 다리에 올라가있는 트럭의 수 비교
				sum += truck_weights[count];
				q.push(truck_weights[count]); count++;
				answer++;
			}
			else {
				sum -= q.front();
				q.pop();
			}

		}
		else {
			if (q.size() < bridge_length) {
				q.push(0);
				answer++;
			}
			else {
				sum -= q.front();
				q.pop();
			}
		}

	}

	return answer + bridge_length;
}