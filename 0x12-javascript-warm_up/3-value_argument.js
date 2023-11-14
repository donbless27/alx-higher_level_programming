#!/usr/bin/node
const firstArgument = process.argv[2];

const message = firstArgument ? firstArgument : "No argument";

console.log(message);

