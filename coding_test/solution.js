const str = "()()()()()()()()";

function solution(str) {
  let result = 0;
  [...str].forEach((i) => {
    if (i === "(") result += 1;
    else result -= 1;
    if (result < 0) return;
  });
  return result >= 0;
}

console.log(solution(str));
