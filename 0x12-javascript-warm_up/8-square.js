#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let i = parseInt(process.argv[2]);
  let j = parseInt(process.argv[2]);
  let kl = '';
  while (i > 0) {
    while (j > 0) {
      kl += 'X';
      j -= 1;
    }
    console.log(kl);
    i -= 1;
  }
}
