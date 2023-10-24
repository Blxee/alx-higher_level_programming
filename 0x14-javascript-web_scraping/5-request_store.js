#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
});
