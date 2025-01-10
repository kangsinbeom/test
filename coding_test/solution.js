function solution(n, k) {
  const people = Array.from({ length: n }, (_, index) => index + 1);
  let count = 1;
  while (people.length > 1) {
    if (count === k) {
      people.shift();
      count = 0;
    } else {
      people.push(people.shift());
    }
    count++;
  }
  return people[0];
}

console.log(solution(5, 2));
