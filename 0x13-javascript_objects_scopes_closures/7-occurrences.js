#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (list === undefined) {
    return 0;
  }
  return list.reduce((acc, cur) => {
    if (cur === searchElement) {
      return acc + 1;
    }
    return acc;
  }, 0);
};
