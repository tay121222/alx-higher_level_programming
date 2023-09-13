#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let temp = parseInt(process.argv[2]);
  let temp2 = parseInt(process.argv[3]);

  if (temp < temp2) {
    [temp, temp2] = [temp2, temp];
  }
  for (let i = 4; i < process.argv.length; i++) {
    const current = parseInt(process.argv[i]);
    if (current > temp) {
      temp2 = temp;
      temp = current;
    } else if (current > temp2 && current !== temp) {
      temp2 = current;
    }
  }

  console.log(temp2);
}
