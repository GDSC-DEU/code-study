class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }
  size() {
    // rear가 가리키는 값이 없을 때 아무 데이터가 없는 경우
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  }

  add(value) {
    if (this.size() === 0) {
      this.storage['0'] = value;
    } else {
      this.rear += 1;
      this.storage[this.rear] = value;
    }
  }

  popFront() {
    let temp;
    if (this.front === this.rear) {
      temp = this.storage[this.front];
      delete this.storage[this.front];
      this.front = 0;
      this.rear = 0;
    } else {
      temp = this.storage[this.front];
      delete this.storage[this.front];
      this.front += 1;
    }
    return temp;
  }
}

function solution(progresses, speeds) {
  let queue = new Queue();
  progresses.forEach((progress, index) => {
    queue.add([progress, speeds[index]]);
  });

  let days = 0;
  let count;
  var answer = [];

  while (queue.size() > 0) {
    count = 0;
    while (
      queue.storage[queue.front][0] + queue.storage[queue.front][1] * days >=
      100
    ) {
      queue.popFront();
      count += 1;
      if (queue.size() === 0) {
        break;
      }
    }
    if (count !== 0) {
      answer.push(count);
    }
    days++;
  }
  return answer;
}
