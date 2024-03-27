#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  const films = JSON.parse(body).results;
  const filmsWithWedge = films.filter(film => film.characters.includes(characterId));

  console.log(filmsWithWedge.length);
});
