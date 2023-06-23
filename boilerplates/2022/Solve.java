import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Solve {
  public static void main(String[] args) throws IOException {
    BufferedReader input = null;

    try {
      input = new BufferedReader(new FileReader("input"));

      String line;
      while ((line = input.readLine()) != null) {

      }
    } finally {
      if (input != null) {
        input.close();
      }
    }
  }
}
