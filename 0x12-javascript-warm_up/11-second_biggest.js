#!/usr/bin/node

// Retrieve the arguments and convert them to integers
const numbers = process.argv.slice(2).map(arg => parseInt(arg));

const sortedNumbers = numbers.sort((a, b) => b - a);
if (sortedNumbers.length <= 1) {
    console.log(0);
}
else {
    console.log(sortedNumbers[1]);
}

