#!/usr/local/bin/node
// a script that display the status code of a GET request
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs, log the error
    console.error('Error:', error);
    return;
  }
  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
