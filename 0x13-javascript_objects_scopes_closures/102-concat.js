#!/usr/bin/node

const fs = require('fs');
const [inFile1, inFile2, outFile] = process.argv.slice(2);

fs.readFile(inFile1, 'utf8', (err, data1) => {
  if (err) {
    console.log(`[Error]: couldn't read ${inFile1}!`);
    process.exit();
  }

  fs.readFile(inFile2, 'utf8', (err, data2) => {
    if (err) {
      console.log(`[Error]: couldn't read ${inFile2}!`);
      process.exit();
    }

    fs.writeFile(outFile, data1 + data2, 'utf8', (err, data2) => {
      if (err) {
        console.log(`[Error]: couldn't write to ${outFile}!`);
        process.exit();
      }
    });
  });
});
