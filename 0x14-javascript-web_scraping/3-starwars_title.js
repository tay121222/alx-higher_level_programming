#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.error(error);
  }
});
