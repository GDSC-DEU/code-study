function solution(participant, completion) {
  for (let person of participant) {
    if (completion.includes(person)) {
      completion.splice(completion.indexOf(person), 1);
    } else return person;
  }
}
