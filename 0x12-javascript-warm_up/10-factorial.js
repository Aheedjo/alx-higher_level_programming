#!/usr/bin/node

function rFactorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * rFactorial(n - 1));
}

console.log(rFactorial(Number(process.argv[2])));

