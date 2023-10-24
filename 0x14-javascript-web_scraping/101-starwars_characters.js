#!/usr/bin/node
const request = require('request');

const film = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
const options = { json: true };
let len = 0;
let characters = [];

request(film, options, (err, response, body) => {
  len = body.characters.length;
  characters = body.characters;
  if (!err) {
    recurse(0);
  }
});

function recurse (index) {
  request(characters[index], options, (err, response, body) => {
    if (!err) {
      console.log(body.name);
      if (index < len - 1) {
        recurse(index + 1);
      }
    }
  });
}
