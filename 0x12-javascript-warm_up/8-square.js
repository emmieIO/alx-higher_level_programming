#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (!arg) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
