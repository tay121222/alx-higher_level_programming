#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`) ? acc + 1 : acc;
    }, 0);
    console.log(count);
  } else {
    console.error(error);
  }
});
