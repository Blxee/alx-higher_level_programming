#!/usr/bin/node
let arr = process.argv.slice(2);
arr = arr
  .map(n => parseInt(n))
  .filter(n => !isNaN(n));
arr.pop(Math.max(...arr));
console.log(Math.max(...arr));
