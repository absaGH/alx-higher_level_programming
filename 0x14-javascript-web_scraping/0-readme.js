#!/usr/bin/node
const flname = require('flname');
flname.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
