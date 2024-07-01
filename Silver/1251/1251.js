let fs = require("fs")
/* 제출용 */
let input = fs.readFileSync('/dev/stdin').toString().trim();
/* 테스트용 */
// let input = fs.readFileSync(__dirname + '/input.txt').toString();
let stringLen = input.length;
let answerList = [];

for(let i=1; i<stringLen-1; i++){
  for(let j=i+1; j<stringLen; j++){
    const first = input.slice(0, i).split("").reverse().join("");
    const second = input.slice(i, j).split("").reverse().join("");
    const last = input.slice(j, stringLen).split("").reverse().join("");

    answerList.push(first+ second+last);
  }
}

answerList = answerList.sort();
console.log(answerList[0]);
