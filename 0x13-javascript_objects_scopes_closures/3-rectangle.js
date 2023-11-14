#!/usr/bin/node
// A Rectangle class that defines a rectangle
class Rectangle {
  constructor(w, h) {
    // Constructor function
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      // Check if the provided parameters are valid
      this.width = w;
      this.height = h;
    }
  }

  print() {
    // Method to print a rectangle
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += 'X';
        y++;
      }
      console.log(myVar);
    }
  }
}

module.exports = Rectangle;
