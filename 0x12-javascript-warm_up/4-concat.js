#!/usr/bin/node

function printfis () {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log('undefined is undefined');
  } else {
    console.log(args.join(' is '));
  }
}

printfis();
