#!/usr/bin/node
// a script that returns a Star Wars movie with a given episode number
const request = require('request');

const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
