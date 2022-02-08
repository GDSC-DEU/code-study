function hashing(clothes) {
  let hashTable = {};
  for (let kind of clothes) {
    if (hashTable[kind[1]]) hashTable[kind[1]] += 1;
    else hashTable[kind[1]] = 1;
  }
  return hashTable;
}

function solution(clothes) {
  let hashTable = hashing(clothes);
  var answer = 1;
  for (let key in hashTable) {
    answer *= hashTable[key] + 1;
  }
  answer -= 1;
  return answer;
}
