#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      Object.assign(this, {});
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      console.log('Empty object');
    }
  }
}
module.exports = Rectangle;
