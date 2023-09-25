#!/usr/bin/node
exports.converter = function (base) {
  if (base < 2 || base > 36) return (number) => number.toString();
  return (number) => number.toString(base);
};
