#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const options = { json: true };

request(url, options, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(body.title);
});
