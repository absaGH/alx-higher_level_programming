#!/usr/bin/node
let secondMax = 0;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const vals = process.argv.slice(2).sort((a, b) => a - b);
  secondMax = vals[vals.length - 2];
  console.log(secondMax);
}
