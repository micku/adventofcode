import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.TreeSet;

public class Solve {
  public static void main(String[] args) throws IOException {
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
  }
}
