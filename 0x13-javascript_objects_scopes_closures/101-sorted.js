#!/usr/bin/node
const dict = require('./101-data').dict;
const obj = {};
for (const key in dict) {
  const value = dict[key];
  if (!(value in obj)) {
    obj[value] = [key];
  } else {
    obj[value].push(key);
  }
}
console.log(obj);
