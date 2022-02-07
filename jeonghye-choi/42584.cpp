//---------------------------------------------------------------------------
// Title:         프로그래머스 스택/큐 주식가격
// Author:        jeonghye-choi
// Last Updated:  2022.2.8
// Link:          https://programmers.co.kr/learn/courses/30/lessons/42584
//---------------------------------------------------------------------------

#include <iostream>
#include <vector>
using namespace std;

vector<int> solution(vector<int> prices) {
  vector<int> answer;
  vector<int>::iterator current_iter;
  int period;

  for (vector<int>::iterator iter=prices.begin(); iter != prices.end(); iter++){
    current_iter = iter;
    period = 0;

    while (current_iter != prices.end()-1){
      if (*current_iter >= *iter){
        period++;
      } else {
        break;
      }
      current_iter++;
    }
    answer.push_back(period);
  }

  return answer;
}

vector<int> prices {1, 2, 3, 2, 3};

int main(){
  solution(prices);

  return 0;
}

