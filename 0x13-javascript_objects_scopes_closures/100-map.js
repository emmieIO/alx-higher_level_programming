#!/usr/bin/node
const list = require('./tests/100-data').list;

console.log(list);
console.log(list.map((item, index) => item * index));
