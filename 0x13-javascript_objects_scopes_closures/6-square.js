#!/usr/bin/node

const PreSquare = require('./5-square');

class Square extends PreSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let _i = 0; _i < this.height; _i++) {
        for (let _j = 0; _j < this.width; _j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
