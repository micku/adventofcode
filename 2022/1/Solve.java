import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.TreeSet;

public class Solve {
  public static void main(String[] args) throws IOException {
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
  }
}
