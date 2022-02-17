#include <string>
#include <vector>
#include<algorithm>
using namespace std;

bool compare(string s1, string s2) {
    return s1 + s2 > s2 + s1;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    for (auto num:numbers) {
        v.push_back(to_string(num));
    }
    
    sort(v.begin(), v.end(), compare);

    if (v[0] == "0") return "0";

    for (auto i:v) {
        answer += i;
    }
    return answer;
}