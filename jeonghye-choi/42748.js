//---------------------------------------------------------------------------
// Title:         프로그래머스 정렬 K번째수
// Author:        jeonghye-choi
// Last Updated:  2022.2.14
// Link:          https://programmers.co.kr/learn/courses/30/lessons/42748
//---------------------------------------------------------------------------

function solution(array, commands) {
  return commands.map(
    (command) =>
      array.slice(command[0] - 1, command[1]).sort((a, b) => a - b)[
        command[2] - 1
      ]
  );
}
