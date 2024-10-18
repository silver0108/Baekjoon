const fs = require("fs");

/* 제출용 */
const input = fs.readFileSync("/dev/stdin").toString().trim();
/* 테스트용 */
// let input = fs.readFileSync(__dirname + "/input.txt").toString();

const [n, m] = input.split(" ").map(Number);

const result = [];
const visited = new Array(n + 1).fill(false);

const dfs = (k, start) => {
  if (k === m) {
    console.log(`${result.join(" ")}`);
    return;
  }
  for (let i = start; i < n; i++) {
    if (!visited[i]) {
      result.push(i + 1);
      visited[i] = true;
      dfs(k + 1, i);
      // 백트래킹
      result.pop();
      visited[i] = false;
    }
  }
};

dfs(0, 0);
