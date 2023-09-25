#!/usr/bin/node
const Squaree = require('./5-square.js');

module.exports = class Square extends Squaree {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
