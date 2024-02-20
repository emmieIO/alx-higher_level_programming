#!/usr/bin/node
const url = process.argv[2];
const req = require('request');

req.get(url)
  .on('response', function (response) {
    console.log('code:', response && response.statusCode);
  });
