//---------------------------------------------------------------------------
// Title:         프로그래머스 완전탐색 모의고사
// Author:        jeonghye-choi
// Last Updated:  2022.2.22
// Link:          https://programmers.co.kr/learn/courses/30/lessons/42840
//---------------------------------------------------------------------------

function solution(answers) {
  let count = [0, 0, 0];
  let result = [];

  const student1 = [1, 2, 3, 4, 5]; // 5개 반복
  const student2 = [2, 1, 2, 3, 2, 4, 2, 5]; //8개 반복
  const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; // 10개 반복

  answers.forEach((answer, index) => {
    if (student1[index % 5] === answer) {
      count[0] += 1;
    }
    if (student2[index % 8] === answer) {
      count[1] += 1;
    }
    if (student3[index % 10] === answer) {
      count[2] += 1;
    }
  });

  var max = 0;
  count.forEach((value, index) => {
    if (value > max) {
      max = value;
      result = [index + 1];
    } else if (value === max) {
      result.push(index + 1);
    }
  });

  return result;
}

const answers = [1, 3, 2, 4, 2];
solution(answers);
