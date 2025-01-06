const string = "[](){}";

function solution(string) {
  let result = 0;
  const array = [...string];
  for (let i = 0; i < array.length; i++) {
    const stack = [];
    // forEach 안에서는 break 못쓴다. forEach는 내부적으로 콜백함수로 구현되어 있기 때문
    array.forEach((value) => {
      if (stack.length === 0) {
        stack.push(value);
      } else {
        if (value === "]" && stack[stack.length - 1] === "[") stack.pop();
        else if (value === "}" && stack[stack.length - 1] === "{") stack.pop();
        else if (value === ")" && stack[stack.length - 1] === "(") stack.pop();
        else stack.push(value);
      }
    });
    if (stack.length === 0) result++; // JS에서는 빈 배열은 true이니 이거 조심하자
    array.push(array.shift());
  }

  return result;
}
console.log(solution(string));
