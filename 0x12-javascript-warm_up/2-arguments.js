#!/usr/bin/node
const numArguments = process.argv.length - 2;
const message =
  numArguments === 0 ? "No argument" :
  numArguments === 1 ? "Argument found" :
  "Arguments found";
console.log(message);
