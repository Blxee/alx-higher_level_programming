#!/usr/bin/node
const request = require('request');

const film = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
const url = 'https://swapi-api.alx-tools.com/api/people/';
const options = { json: true };

request(url, options, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  for (const character of body.results) {
    if (character.films.includes(film)) {
      console.log(character.name);
    }
  }
});
