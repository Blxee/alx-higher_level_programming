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
  let n = 0;
  for (const film of body.results) {
    if (film.characters.includes(charUrl)) {
      n++;
    }
  }
  console.log(n);
});
