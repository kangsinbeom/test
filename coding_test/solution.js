function solution() {
  const mock_answer = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5];
  const patterns = ["12345", "21232425", "3311224455"];
  let scores = new Array(3).fill(0);
  mock_answer.forEach((answer, i) => {
    patterns.forEach((str, j) => {
      const pattern = [...str];
      if (answer === parseInt(pattern[i % pattern.length])) {
        scores[j] += 1;
      }
    });
  });
  return scores;
}

console.log(solution());
