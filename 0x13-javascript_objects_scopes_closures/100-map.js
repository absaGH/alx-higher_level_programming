#!/usr/bin/node
const new_list = require('./100-data.js').list;
console.log(new_list);
console.log(new_list.map((item, index) => item * index));
