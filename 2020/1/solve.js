const fs = require("fs");
const path = require("path");

const part1 = (input) => {
  const entries = input.map((x) => parseInt(x));

  while ((entry = parseInt(entries.pop()))) {
    const diff = 2020 - entry;

    if (entries.indexOf(diff) >= 0) {
      return entry * diff;
    }
  }
  return null;
};

const part2 = (input) => {
  const entries = input.map((x) => parseInt(x));

  while ((entry = parseInt(entries.pop()))) {
    const secondEntries = [...entries];

    while ((secondEntry = parseInt(secondEntries.pop()))) {
      const diff = 2020 - entry - secondEntry;

      if (secondEntries.indexOf(diff) >= 0) {
        return entry * secondEntry * diff;
      }
    }
  }
  return null;
};

const inputPath = path.join(__dirname, "input");
const inputFile = fs
  .readFileSync(inputPath, "utf8")
  .split("\n")
  .filter((a) => a !== "");

const solution1 = part1([...inputFile]);
if (solution1 !== null) {
  console.log(`  Solution for part 1 is: ${solution1}`);
}

const solution2 = part2([...inputFile]);
if (solution2 !== null) {
  console.log(`  Solution for part 2 is: ${solution2}`);
}
