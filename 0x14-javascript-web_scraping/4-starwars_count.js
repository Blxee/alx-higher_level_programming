#!/usr/bin/node
const request = require('request');

const filmsUrl = process.argv[2];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const options = { json: true };

request(filmsUrl, options, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const n = body.results.reduce((acc, film) => {
    if (film.characters.some(char => char == charUrl)) {
      return acc + 1;
    }
    return acc;
  }, 0);
  console.log(n);
});
