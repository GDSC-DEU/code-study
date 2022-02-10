#include <string>
#include <vector>
#include<queue>
#include<iostream>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    queue<int>q;
    int count=0,size=prices.size(),now=0,index=0;

    for (int i = 0; i < size; i++)q.push(prices[i]);
    
    while (!q.empty()) {
        now = q.front();
        count = 0; 
        for (int i = answer.size()+1; i < size; i++) {
            count++;
            if (prices[i] < now) break;
           
        }
        q.pop();
        answer.push_back(count);
    }
    
    
    return answer;
}