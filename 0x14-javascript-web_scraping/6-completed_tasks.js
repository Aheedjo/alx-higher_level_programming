#!/usr/bin/node
// a script that computes the number of tasks completed by user id
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  let data = [];
  try {
    data = JSON.parse(body); // Convert the JSON string to a JavaScript object
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    return;
  }

  const result = {};
  for (const task of data) {
    if (task.completed) {
      if (result[task.userId]) result[task.userId]++;
      else result[task.userId] = 1;
    }
  }
  console.log(result);
});
