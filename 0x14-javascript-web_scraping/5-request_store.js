#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const [url, filePath] = process.argv.slice(2);

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
