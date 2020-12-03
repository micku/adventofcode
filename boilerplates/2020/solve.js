const fs = require("fs");
const path = require("path");

const part1 = (input) => {
  return null;
};

const part2 = (input) => {
  return null;
};

const inputPath = path.join(__dirname, "input");
const inputFile = fs
  .readFileSync(inputPath, "utf8")
  .split("\n")
  .filter((a) => a !== "");

const solution1 = part1(inputFile);
if (solution1 !== null) {
  console.log(`  Solution for part 1 is: ${solution1}`);
}

const solution2 = part2(inputFile);
if (solution2 !== null) {
  console.log(`  Solution for part 2 is: ${solution2}`);
}
