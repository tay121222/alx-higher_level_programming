#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (process.argv[2]) {
  console.log(factorial(parseInt(process.argv[2])));
} else { console.log(1); }
