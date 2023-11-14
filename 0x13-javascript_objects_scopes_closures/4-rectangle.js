#!/usr/bin/node

// Defines a Rectangle class
class Rectangle {
  /**
   * Constructor for the Rectangle class
   * @param {number} w - Width of the rectangle
   * @param {number} h - Height of the rectangle
   */
  constructor(w, h) {
    // Check if the provided parameters are valid numbers greater than 0
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      // If valid, initialize the instance attributes
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Print a rectangle made of 'X' characters to the console
   */
  print() {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      // Fill each row with 'X' characters (this.width times)
      while (y < this.width) {
        myVar += 'X';
        y++;
      }

      // Print the row to the console
      console.log(myVar);
    }
  }

  /**
   * Rotate the rectangle by swapping the values of width and height
   */
  rotate() {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  //Double the dimensions of the rectangle
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

// Export the Rectangle class for use in other modules
module.exports = Rectangle;

