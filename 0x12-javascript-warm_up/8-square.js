#!/usr/bin/node
const dimension = Math.floor(Number(process.argv[2]));
if (isNaN(dimension)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < dimension; r++) {
    let row = '';
    for (let i = 0; i < dimension; i++) row += 'X';
    console.log(row);
  }
}
