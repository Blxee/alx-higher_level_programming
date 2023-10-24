#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const options = { json: true };

request(url, options, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasksDone = {};
  for (const task of body) {
    if (task.completed) {
      if (!(task.userId in tasksDone)) {
        tasksDone[task.userId] = 0;
      }
      tasksDone[task.userId] += 1;
    }
  }
  console.log(tasksDone);
});
