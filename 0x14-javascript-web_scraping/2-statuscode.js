#!/usr/bin/node
const url = process.argv[2];
const req = require('request')

req(url, function (error, response, body) {
  console.log('code:', response && response.statusCode);
});
