#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int s1[5] = {1, 2, 3, 4, 5};
int s2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
int s3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> solution(vector<int> answers) {
    int check[3] = {0, };
    int best=0;
    vector<int> answer;
    
    for(int i = 0; i < answers.size(); i++){
        if(s1[i % 5] == answers[i])  
            check[0]++;
        if(s2[i % 8] == answers[i])
            check[1]++;
        if(s3[i % 10] == answers[i])
            check[2]++;
    }
    
    best = max(max(check[0], check[1]), check[2]);
    
    for(int i = 0; i < 3; i++){
       if(check[i] == best) {
           answer.push_back(i + 1);
       }
   }
    
    return answer;
}