#include <string>
#include <vector>
#include<algorithm>
#include<iostream>
using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int supo1[5] = { 1,2,3,4,5 };
    int supo2[8] = { 2, 1, 2, 3, 2, 4, 2, 5 };
    int supo3[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };
    int scores[3] = { 0,0,0 },max_score=0;
    
    for (int i = 0; i < answers.size(); i++) {

        if (supo1[i % 5] - answers[i] == 0)
            scores[0]++;

        if (supo2[i % 8] - answers[i] == 0)
            scores[1]++;

        if (supo3[i % 10] - answers[i] == 0)
            scores[2]++;

    }
    
    max_score = max(scores[0], max(scores[1], scores[2]));

    for (int i = 0; i < 3; i++) {
        if (max_score - scores[i] == 0)
            answer.push_back(i+1);
    }       
    return answer;
}