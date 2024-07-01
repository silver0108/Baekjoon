// 막대기

const fs = require("fs");
/* 제출용 */
let input = fs.readFileSync('/dev/stdin').toString().trim();
/* 테스트용 */
// let input = fs.readFileSync(__dirname + '/input.txt').toString().trim();
let X = Number(input);
let bar = 64;
let count = 0;

while(true) {
  if (bar === X) {
    count++;
    break;
  }
  else if (bar > X) {
    bar /= 2;
  }else {
    count++;
    X -= bar;
  }
}

console.log(count);