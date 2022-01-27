#include <string>
#include <vector>
#include<stack>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer = { 1 }; //0번째 배열에 있는 기능이 완성될때 
	int time = (99 - progresses[0]) / speeds[0] + 1, count = 0;  //0번째 기능이 완성되는 시간을 time으로
	stack<int> s;
	s.push(time);  // 0번째 기능이 완성되는 시간을 스택에 push
	for (int i = 1; i < progresses.size(); i++) {
		time = (99 - progresses[i]) / speeds[i] + 1; //그다음 기능이 완성되는 시간을 time에 저장
		// 시간 비교
        if (s.top() < time) { 
			s.push(time);
			answer.push_back(0);
			answer[++count]++;
		}
		else answer[count]++; // 그 다음 기능이 완성되는 시간이 더 짧은 경우
	}

	return answer;
}