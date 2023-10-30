#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      const characters = film.characters;
      characters.forEach((character) => {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  } else {
    console.log(err);
  }
});
