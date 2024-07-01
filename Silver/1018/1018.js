// 체스판 다시 칠하기

const fs = require("fs");
/* 제출용 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
/* 테스트용 */
// let input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split('\n').map(line => line.replace('\r', ''));
const [size, ...arr] = input;
const [N, M] = size.split(' ').map(Number);
const answer = [];

const whiteFirstBorad = [
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
];
const balckFirstBoard = [
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
];
// 하얀색이 먼저 시작하는 체스판과 비교
const whiteFirst = (x, y) => {
  let count = 0;
  for(let i=0; i<8; i++){
    for(let j=0; j<8; j++){
      if(arr[x+i][y+j] != whiteFirstBorad[i][j]) count++;
    }
  }
  return count;
}
// 검은색이 먼저 시작하는 체스판과 비교
const blackFirst = (x, y) => {
  let count = 0;
  for(let i=0; i<8; i++){
    for(let j=0; j<8; j++){
      if(arr[x+i][y+j] != balckFirstBoard[i][j]) count++;
    }
  }
  return count;
}

// 전체 판을 벗어나지 않도록 +7한 값이 보드판 사이즈보다 작도록
for(let i=0; i + 7 < N; i++){
  for(let j=0; j + 7 < M; j++){
    answer.push(whiteFirst(i, j));
    answer.push(blackFirst(i, j));
  }
}

console.log(Math.min(...answer))