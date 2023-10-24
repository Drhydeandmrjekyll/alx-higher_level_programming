#!/usr/bin/node


const request = require('request');

// Import 'request' module.


request.get(process.argv[2])

// Use 'request' module to perform an HTTP GET request to URL.


  .on('response', function (response) {

    // Set up an event listener for 'response' event emitted by HTTP request.


    console.log(`code: ${response.statusCode}`);

    // Log HTTP status code of response to console.

  });
