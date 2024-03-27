#!/usr/bin/node
const request = require('request');

const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
