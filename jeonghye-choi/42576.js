function hashing(completion) {
  let hashTable = {};
  for (let person of completion) {
    if (hashTable[person]) hashTable[person] += 1;
    else hashTable[person] = 1;
  }
  return hashTable;
}

function solution(participant, completion) {
  let hashTable = hashing(completion);

  for (let person of participant) {
    if (!hashTable[person] || hashTable[person] === 0) return person;
    else hashTable[person] -= 1;
  }
}
