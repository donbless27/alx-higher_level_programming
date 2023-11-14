#!/usr/bin/node
// a script that concats 2 files
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 5) {
    console.log('Usage: node concatFiles.js <fileA> <fileB> <fileC>');
    process.exit(1);
}

// Check if fileA and fileB exist and are valid files
if (
    fs.existsSync(fileA) &&
    fs.statSync(fileA).isFile() &&
    fs.existsSync(fileB) &&
    fs.statSync(fileB).isFile() &&
    fileC !== undefined
) {
        // Read the contents of fileA and fileB
        const fileAContent = fs.readFileSync(fileA);
        const fileBContent = fs.readFileSync(fileB);

        // Create a write stream for fileC
        const stream = fs.createWriteStream(fileC);

        // Write the contents of fileA and fileB to fileC
        stream.write(fileAContent);
        stream.write(fileBContent);

        // Close the write stream
        stream.end();
}
