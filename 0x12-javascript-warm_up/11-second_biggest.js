#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const temp = parseInt(process.argv[2]);
  let temp2 = parseInt(process.argv[3]);

  for (let i = 4; i < process.argv.length; i++) {
    const current = parseInt(process.argv[i]);
    if (current > temp) {
      temp2 = temp;
    } else if (current > temp2 && current !== temp) {
      temp2 = current;
    }
  }

  console.log(temp2);
}
