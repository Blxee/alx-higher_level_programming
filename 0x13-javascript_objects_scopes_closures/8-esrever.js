#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((a, i) => {
    a.unshift(i);
    return a;
  }, []);
};
