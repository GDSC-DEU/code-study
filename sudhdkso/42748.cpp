#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
 
    for (int i = 0;i < commands.size();i++) {
        int Fidx = commands[i][0] - 1;
        int Lidx = commands[i][1] - 1;
        int idx = commands[i][2]-1;
        vector <int> a;
        for (int j = Fidx;j < Lidx + 1;j++)
            a.push_back(array[j]);

        sort(a.begin(), a.end());

        answer.push_back(a[idx]);
    }

    return answer;
}