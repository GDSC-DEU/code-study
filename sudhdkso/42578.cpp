#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> hash;

    for (int i = 0; i < clothes.size(); i++) {
        if (hash.find(clothes[i][1]) == hash.end()) {
            hash.insert({ clothes[i][1],1});
        }

        else
            hash[clothes[i][1]]++;
    }

    for (auto it : hash) {
        answer *= it.second+1;
    }
            

    return answer-1;
}