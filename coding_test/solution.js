const number = 12;

function solution(number) {
  const stack = [];
  while (!!number) {
    stack.push(number % 2);
    number = ~~(number / 2);
  }
  return stack.reduce((acc, curr) => acc + curr, "");
}

console.log(solution(number));
