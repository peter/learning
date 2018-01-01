import java.util.ArrayList;
import java.util.Scanner;

// Basic value object class
class Data {
  protected Object data;

  public Data(Object data) {
    this.data = data;
  }
}

// Class inheritance with extends and super
class Line extends Data {
  public Line(String line) {
    super(line);
  }

  // Overriding toString to do something useful
  public String toString() {
    return data.toString();
  }
}

// Compile/run with:
// javac -Xlint Tutorial.java && cat Tutorial.java | java -ea Tutorial arg1 arg2
public class Tutorial {
  public static final double PI = 3.141597;

  public static void main(String[] args) {
    printHeader("Command line args");
    System.out.println(String.join(", ", args));

    printHeader("Reading stdin");
    Scanner scanner = new Scanner(System.in);
    ArrayList<Line> lines = new ArrayList<Line>();
    while (scanner.hasNext()) lines.add(new Line(scanner.nextLine()));
    for (Line line : lines) {
      System.out.println(line);
    }

    printHeader("Checking class membership of object with instanceof");
    Exception e = new Exception("foobar");
    if (e instanceof RuntimeException) {
      System.out.println("e is a runtime exception");
    } else {
      System.out.println("e is *not* a runtime exception");
    }

    printHeader("Iterating over chars of a string and using StringBuilder");
    StringBuilder sb = new StringBuilder();
    String myString = "foobar";
    for (int i = 0; i < myString.length(); i++) {
      char c = myString.charAt(i);
      sb.append(Character.toUpperCase(c));
    }
    System.out.println("StringBuilder: " + sb.toString());

    printHeader("Null check with assert");
    assert sb != null;
    // NOTE: failed assertions throw java.lang.AssertionError if you have -ea (Enable Assertions) in your JVM options
    // assert sb.length() > 100000;

    // Ternary operator
    // return codeSource == null ? null : codeSource.getLocation();

    // Exception handling
//    try {
//      Class.forName("com.carrotsearch.randomizedtesting.RandomizedContext");
//    } catch (final ClassNotFoundException e) {
//      // we are not in tests but build.snapshot is set, bail hard
//      throw new IllegalStateException("build.snapshot set to [" + buildSnapshot + "] but not running tests");
//    }
  }

  public static void printHeader(String header) {
    System.out.println("\n## " + header + "\n");
  }
}
