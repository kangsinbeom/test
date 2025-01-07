const s = "baabaa";

function solution(string) {
  const stack = [];
  [...string].forEach((i) => {
    if (stack.length !== 0 && stack[stack.length - 1] === i) {
      stack.pop();
    } else stack.push(i);
    console.log(stack);
  });
  return !stack.length ? 1 : 0;
}
console.log(solution(s));
