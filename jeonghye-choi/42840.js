//---------------------------------------------------------------------------
// Title:         프로그래머스 완전탐색 모의고사
// Author:        jeonghye-choi
// Last Updated:  2022.2.22
// Link:          https://programmers.co.kr/learn/courses/30/lessons/42840
//---------------------------------------------------------------------------

function solution(answers) {
  let count = [0, 0, 0];
  let result = [];

  const students = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  answers.forEach((answer, answerIndex) => {
    students.forEach((student, studentIndex) => {
      if (student[answerIndex % student.length] === answer) {
        count[studentIndex] += 1;
      }
    });
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
