#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
req.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, req, res) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(req.body);
  console.log(data.title);
});
