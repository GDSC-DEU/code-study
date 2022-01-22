#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string &a, string &b){
    if (a.length() != b.length()) return a.length() < b.length();
    else return a < b;
}

bool check(vector<string> phone_book, string & prefix, int & index){
    for(int i=index+1; i < phone_book.size(); i++){
        if (prefix == phone_book[i].substr(0,prefix.size())){
            return false;
        }
    }
    return true;
}

bool solution(vector<string> phone_book) {
    // 1 문자열 길이 순대로 정렬
    sort(phone_book.begin(), phone_book.end(),cmp);

    // 2 반복문을 돌면서 prefix 확인
    bool answer = true;
    int index=0;
    for (auto phone : phone_book){
        answer = check(phone_book, phone, index);
        if(!answer) break;
        index++;
    }
    return answer;
}