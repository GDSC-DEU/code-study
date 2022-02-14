#include <string>
#include <vector>
#include<queue>
#include<iostream>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0,sum=0;
    priority_queue<int, vector<int>, greater<int>>pq(scoville.begin(),scoville.end());

    while (pq.size()>1 && pq.top()<K) {
        sum = pq.top(); pq.pop(); sum += (pq.top()*2); pq.pop();
        pq.push(sum);
        answer++;

    }

    if (pq.top() < K) return -1;

    return answer;
}