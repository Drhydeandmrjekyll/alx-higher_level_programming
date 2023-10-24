#!/usr/bin/node


// Import 'request' module

const request = require('request');


// Use 'request' module to perform an HTTP GET request to URL

request(process.argv[2], function (error, response, body) {

  // Check if there was no error during HTTP request.

  if (!error) {

    // parse JSON data and extract "results" array

    const results = JSON.parse(body).results;

    // Use 'reduce()' method to iterate through movies in 'results' array.

    console.log(results.reduce((count, movie) => {

      // check if there is character with ID 18 ('/18/') in 'characters' array.

      return movie.characters.find((character) => character.endsWith('/18/'))

        // If character with ID 18 is found, increment count by 1.

        ? count + 1

        // Otherwise, keep count unchanged.

        : count;

      // The 'reduce()' method starts with initial value of 0 ('0' at the end).

    }, 0));

  }

});
