#!/usr/bin/node
exports.converter = function (base) {
  function convto (val) {
    return val.toString(base);
  }
  return convto;
};
