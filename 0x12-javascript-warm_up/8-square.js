#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('#');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
