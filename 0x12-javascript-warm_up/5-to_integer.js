#!/usr/bin/node
const numArgs = Math.floor(Number(process.argv[2]));
if (isNaN(numArgs)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numArgs);
}
