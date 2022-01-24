#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> musicMax;
    unordered_map<string, unordered_map<int,int>> hash;
    string str; 
    int max = 0, index = -100, maxPlay = 0;

    for (int i = 0; i < genres.size(); i++) {
        musicMax[genres[i]] += plays[i];
        hash[genres[i]].insert({ i,plays[i] });
        
    }

    while (musicMax.size()>0) {
        str = { NULL }; int max = 0; 
        //가장 많이 재생된 장르를 고름
        for (auto it : musicMax) {
            if (max < it.second) {
                max = it.second;
                str = it.first;
            }
                
        }
        //선택된 장르를 map에서 삭제
        musicMax.erase(str);
        //가장많이 재생된 곡에서 노래 두곡을 선택하는 반복문
        for (int i = 0; i < 2; i++) {
            index = -100; maxPlay = 0;
            //가장 많이 재생된 장르에서 가장 많이 재생된 노래 선택
            for (auto it : hash[str]) {
                if (maxPlay < it.second) {
                    index = it.first;
                    maxPlay = it.second;
                }
                //같은 횟수의 재생곡이 존재할때 고유번호가 낮은 노래 선택
                else if (maxPlay == it.second) {
                    if (index > it.first) {
                        index = it.first;
                    }

                }

            }
            //위의 반복문에 들어가지 않을때, 장르에 수록할 곡이 없는 경우 break;
            if (index == -100) break;
            answer.push_back(index);
            //장르에서 해당 곡 삭제
            hash[str].erase(index);
        }
   }

    return answer;
}