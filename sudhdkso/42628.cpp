#include <string>
#include <vector>
#include<iostream>
#include<queue>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    priority_queue<int, vector<int>, greater<int>> asc;
    priority_queue<int, vector<int>> desc;
    int count = 0;
    for (string p : operations) {

        if(count==0)
        {
            while(!asc.empty()) asc.pop();
            while(!desc.empty()) desc.pop();
        }

        if (p[0] == 'I') {
            desc.push(stoi(p.substr(2))); 
            asc.push(stoi(p.substr(2)));
            count++;
        }
        else {
            if (count<=0) continue;

            if (p[2] == '1') {
                desc.pop();
                count--;
            }

            else {
                asc.pop();
                count--;
            }

        }
    }
    if (count<=0) {
        answer.push_back(0);
        answer.push_back(0);
    }
    else {
        answer.push_back(desc.top());
        answer.push_back(asc.top());
    }

    return answer;
}