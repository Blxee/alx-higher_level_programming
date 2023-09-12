#!/usr/bin/node
let arr = process.argv.slice(2);
arr = arr
  .map(n => parseInt(n))
  .filter(n => !isNaN(n));
if (arr.length <= 1) {
  console.log(0);
} else {
  arr[arr.indexOf(Math.max(...arr))] = -Infinity;
  console.log(arr)
  console.log(Math.max(...arr));
}
