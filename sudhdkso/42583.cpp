#include <string>
#include <vector>
#include<queue>
#include<iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0, count = 0;
	int sum = 0;
	queue<int> q;
	while (1) {

		//cout << count << ":" << truck_weights.size() << " ";

		if (count > truck_weights.size() - 1)
			break;
		if (sum + truck_weights[count] <= weight) {
			if (q.size() < bridge_length) {
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