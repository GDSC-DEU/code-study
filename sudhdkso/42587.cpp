#include <string>
#include <vector>
#include<queue>
#include<iostream>
#include<algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0, index = location;
	queue<int> q;
	vector<int> v = priorities;
	for (int i = 0; i < priorities.size(); i++)
		q.push(priorities[i]);

    //복사한 순서를 내림차순으로 정렬
	sort(v.begin(), v.end(), greater<>());

	while (q.size() > 0) { 
        //priorities에서 제일 큰 값과 큐의 제일 앞을 비교 
		if (q.front() < v[0]) {
			q.push(q.front());
			q.pop();
			if (index <= 0)
				index = q.size() - 1;
			else
				index--;

		}
		else {
			v.erase(v.begin());
			q.pop();
			index--;
			if (index < 0) {
				return priorities.size() - q.size();
			}


		}

	}

	return answer;
}