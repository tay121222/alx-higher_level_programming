#!/usr/bin/node
const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

const data1 = fs.readFileSync(sourceFile1, 'utf8');
const data2 = fs.readFileSync(sourceFile2, 'utf8');

fs.writeFileSync(destinationFile, data1 + data2, 'utf8');
