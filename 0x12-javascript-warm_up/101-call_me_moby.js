#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
  let i = x;
  while (i > 0) {
    theFunction();
    i -= 1;
  }
};
