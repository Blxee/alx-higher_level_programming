#!/usr/bin/node
const request = require('request');

const film = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
const options = { json: true };

request(film, options, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  for (const character of body.characters) {
    request(character, options, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(body.name);
    });
  }
});
