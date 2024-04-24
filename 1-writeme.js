#!/usr/local/bin/node
// a script that writes to a file
const fs = require('fs');

const file = process.argv[2];
const data = process.argv[3];
fs.writeFile(file, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
