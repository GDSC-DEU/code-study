#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n, num;

    for (int i = 0;i < reserve.size();i++) {
        for (int j = 0;j < lost.size();j++) {
         
            if (reserve[i] == lost[j]) {
                
                reserve.erase(reserve.begin() + i);
                lost.erase(lost.begin() + j);
                i--; j--;
                break;
            }

        }

    }

    if (lost.empty())
        return answer;

    answer -= lost.size();
    
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());

    for (int i = 0;i < reserve.size();i++) {
        for (int j = 0;j < lost.size();j++) {
            num = reserve[i] - lost[j];
            
            if (num == (-1) || num == 1) {
                if (reserve[i] > 0 && lost[j] > 0) {
                    answer++;
                    reserve[i] = -1;
                    lost[j] = -1;
                    break;
                }
            }
        }

    }

    return answer;
}