//---------------------------------------------------------------------------
// Title:         프로그래머스 정렬 가장 큰 수
// Author:        jeonghye-choi
// Last Updated:  2022.2.17
// Link:          https://programmers.co.kr/learn/courses/30/lessons/42746
//---------------------------------------------------------------------------

function solution(numbers) {
  return numbers
    .sort(function (x, y) {
      if (x.toString() + y.toString() > y.toString() + x.toString()) {
        return -1;
      } else if (x.toString() + y.toString() < y.toString() + x.toString()) {
        return 1;
      }
    })
    .join('');
}

// const numbers = [9, 90, 60, 3, 33, 36, 5, 1, 10];
// solution(numbers);
