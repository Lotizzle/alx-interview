#!/usr/bin/node
const axios = require('axios');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

axios.get(url)
  .then(response => {
    const characterUrls = response.data.characters;
    const characterPromises = characterUrls.map(url => axios.get(url));

    return Promise.all(characterPromises);
  })
  .then(responses => {
    responses.forEach(response => {
      console.log(response.data.name);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
