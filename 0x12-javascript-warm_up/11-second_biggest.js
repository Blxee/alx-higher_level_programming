#!/usr/bin/node
let arr = process.argv.slice(2);
if (arr.length <= 1) {
  console.log(0);
  process.exit();
}
arr = arr
  .map(n => parseInt(n))
  .filter(n => !isNaN(n));
arr.pop(Math.max(...arr));
console.log(Math.max(...arr));
