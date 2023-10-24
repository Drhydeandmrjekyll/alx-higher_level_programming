#!/usr/bin/node


const fs = require('fs');

// Import built-in Node.js 'fs' module.


fs.readFile(process.argv[2], 'utf8', function (error, content) {

  // Use fs.readFile() to read contents of file specified as command-line argument

  // 'utf8' specifies encoding of file being read


  if (error) {

    // If an error occurs during file read operation, 'error' parameter will contain error object.

    console.error('Error reading the file:', error);


  } else {

    // If file is read successfully, 'content' parameter will contain contents of file as a string.

    console.log(content);

  }

});
