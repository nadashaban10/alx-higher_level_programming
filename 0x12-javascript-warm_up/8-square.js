#!/usr/bin/node
function PrintSqu () {
    const x = parseInt(process.argv[2], 10);
    if (isNaN(x) || x === undefined) {
      console.log('Missing size');
    } else {
      for (let i = 0; i < x; i++) {
        const squaree = x * x;
        console.log(`X * ${squaree}`);
      }
    }
  }
  PrintSqu();
  