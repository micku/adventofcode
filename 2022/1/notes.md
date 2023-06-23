# Advent of Code 2022 - Java - day 1
[Problem statement](https://adventofcode.com/2022/day/1)

## First solution
```
BufferedReader input = null;

try {
  input = new BufferedReader(new FileReader("input"));

  String line;
  Integer elfCalories = 0;
  TreeSet<Integer> elvesCalories = new TreeSet<Integer>();

  while ((line = input.readLine()) != null) {
	if(line.isBlank()) {
	  elvesCalories.add(elfCalories);
	  elfCalories = 0;
	} else {
	  elfCalories += Integer.parseInt(line);
	}
  }

  Iterator<Integer> topCalories = elvesCalories.descendingIterator();
  Integer top3sum = 0;

  for (int i = 0; i < 3; i ++) {
	top3sum += topCalories.next();
  }
  System.out.println(top3sum);
} finally {
  if (input != null) {
	input.close();
  }
}
```

## Other solutions and possible improvements
In [this solution](https://github.com/pvainio/adventofcode/blob/main/2022/java/Day1.java), there are 2 interesting things:
1. The use of `LinkedList`, I opted for reading and sorting while reading, this other solution reads everything in a `LinkedList` and then sorts as needed. I need to check performance wise which one is better;
2. The one-liner to get and sum the highest 3:
	`cals.stream().limit(3).mapToInt(i -> i).sum()`

In [this other solution](https://github.com/BlockyDotJar/AoC_2022/blob/main/src/dev/blocky/aoc/Day_01.java), which seems similar to mine, it is also interesting how they calculate the top 3:
```
List<Integer> top3 = new ArrayList<>(results.subList(results.size() - 3, results.size()));
return top3.stream().mapToInt(Integer::intValue).sum();
```
Also the [use of `continue`](https://github.com/BlockyDotJar/AoC_2022/blob/f6fea5d0347624c263a5764e99503f2823e23f15/src/dev/blocky/aoc/Day_01.java#L53C3-L53C3) in the while loop should be evaluated.

## Improved version
Focusing only on code clarity, I ended up with this solution:
```
BufferedReader input = null;

try {
  input = new BufferedReader(new FileReader("input"));

  String line;
  Integer elfCalories = 0;
  TreeSet<Integer> elvesCalories = new TreeSet<Integer>((i1, i2) -> i2 - i1);

  while ((line = input.readLine()) != null) {
	if(line.isBlank()) {
	  elvesCalories.add(elfCalories);
	  elfCalories = 0;

	  continue;
	}

	elfCalories += Integer.parseInt(line);
  }

  Integer top3sum = elvesCalories
	.stream()
	.limit(3)
	.mapToInt(i -> i).sum();
  System.out.println(top3sum);
} finally {
  if (input != null) {
	input.close();
  }
}
```

What changed:
- Passed a comparator in the `TreeSet` constructor so it doesn't need to be reversed later;
- Replaces the `else` in  the file read with the `continue`;
- Replaced the `Iterator` use with the [`Stream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html).

*I'm not sure performance-wise which is better though.*

> [!FACT] Stream
> A sequence of elements supporting sequential and parallel aggregate operations. The following example illustrates an aggregate operation using Stream and IntStream:
> ```
> int sum = widgets.stream()
>                  .filter(w -> w.getColor() == RED)
>                  .mapToInt(w -> w.getWeight())
>                  .sum();

Next time I will not focus on reading a file, and will count as it is already in memory. This may be lesse efficient (or maybe not), but at least I can explore different implementations without the constraint of the sequential read.
