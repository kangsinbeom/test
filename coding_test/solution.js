N = 5;
stages = [2, 1, 2, 6, 2, 4, 3, 3];

function solution(N, stages) {
  const result = {};
  const challengers = Array.from({ length: N + 2 }).fill(0);
  stages.forEach((stage) => {
    challengers[stage] += 1;
  });
  let total = stages.length;
  for (i = 1; i < N + 1; i++) {
    if (challengers[i] === 0) {
      result[i] = 0;
    } else {
      result[i] = challengers[i] / total;
      total -= challengers[i];
    }
  }
  sortedKeys = Object.entries(result)
    .sort((a, b) => b[1] - a[1])
    .map(([key, _]) => +key);
  return sortedKeys;
}

console.log(solution(N, stages));
