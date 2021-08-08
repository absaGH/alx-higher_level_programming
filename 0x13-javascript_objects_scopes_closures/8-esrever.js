#!/usr/bin/node
exports.esrever = function (list) {
  const revAry = [];
  for (let i = 0; i < list.length; i++) {
    revAry.unshift(list[i]);
  }
  return revAry;
};
