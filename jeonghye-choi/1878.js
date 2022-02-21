//---------------------------------------------------------------------------
// Title:         프로그래머스 알고리즘 문제 해설 나머지 한 점
// Author:        jeonghye-choi
// Last Updated:  2022.2.17
// Link:          https://programmers.co.kr/learn/courses/18/lessons/1878
//---------------------------------------------------------------------------

const X = 0;
const Y = 1;

function solution(v) {
  var uniqueX = v[0][X];
  var uniqueY = v[0][Y];

  if (v[1][X] == uniqueX) {
    uniqueX = v[2][X];
  } else {
    if (v[1][X] == v[2][X]) {
      uniqueX = v[0][X];
    } else {
      uniqueX = v[1][X];
    }
  }

  if (v[1][Y] == uniqueY) {
    uniqueY = v[2][Y];
  } else {
    if (v[1][Y] == v[2][Y]) {
      uniqueY = v[0][Y];
    } else {
      uniqueY = v[1][Y];
    }
  }

  return [uniqueX, uniqueY];
}

// const v = [
//   [3, 4],
//   [1, 4],
//   [3, 10],
// ];

// solution(v);
