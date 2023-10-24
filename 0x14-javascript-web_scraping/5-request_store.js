#!/usr/bin/node

// Import built-in Node.js 'fs' module

const fs = require('fs');

// Import 'request' module

const request = require('request');

// Use 'request' module to perform an HTTP GET request to URL

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
