#include <string>
#include <vector>
#include<unordered_map>
#include<iostream>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_map<string, int> hash;
    for (int i = 0; i < phone_book.size(); i++) {
        hash.insert({ phone_book[i],1 });
    }

    for (int i = 0; i < phone_book.size(); i++) {
        for(int j=0;j<phone_book[i].length(); j++)
            if (hash.find(phone_book[i].substr(0, j)) != hash.end()) {
                return false;
            }
    }
    return answer;
}