#!/usr/bin/node
const request = require('request');

const filmsUrl = process.argv[2];
const options = { json: true };

request(filmsUrl, options, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const n = body.results.reduce((acc, film) => {
    if (film.characters.some(ch => ch.endsWith('/18/'))) {
      return acc + 1;
    }
    return acc;
  }, 0);
  console.log(n);
});
