#!/usr/bin/node

// Retrieve the arguments and convert them to integers
const numbers = process.argv.slice(2).map(arg => parseInt(arg));
// Replace occurrences of 12 with 89
const modifiedNumbers = numbers.map(num => (num === 12) ? 89 : num);
const sortedNumbers = modifiedNumbers.sort((a, b) => b - a);
if (sortedNumbers.length <= 1) {
    console.log(0);
}
else {
    console.log(sortedNumbers[1]);
}

