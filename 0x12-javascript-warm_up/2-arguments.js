#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments Found');
}
