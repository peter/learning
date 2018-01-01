import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.Collection;

public class Evaluate {
  public static void main(String[] args) {
      Stack<String> ops = new Stack<String>();
      Stack<Double> vals = new Stack<Double>();
      List<String> tokens = tokenize(args[0]);
      for (String s : tokens) {
        if (s.equals("(")) ;
        else if (s.equals("+")) ops.push(s);
        else if (s.equals("-")) ops.push(s);
        else if (s.equals("*")) ops.push(s);
        else if (s.equals("/")) ops.push(s);
        else if (s.equals("sqrt")) ops.push(s);
        else if (s.equals(")")) {
          evaluate(ops, vals);
        }
        else vals.push(Double.parseDouble(s));
      }
      while (!ops.isEmpty()) evaluate(ops, vals);
      StdOut.println(vals.pop());
  }

  private static void evaluate(Stack<String> ops, Stack<Double> vals) {
    String op = ops.pop();
    double v = vals.pop();
    if (op.equals("+")) v = vals.pop() + v;
    else if (op.equals("-")) v = vals.pop() - v;
    else if (op.equals("*")) v = vals.pop() * v;
    else if (op.equals("/")) v = vals.pop() / v;
    else if (op.equals("sqrt")) v = Math.sqrt(v);
    vals.push(v);
  }

  private static List<String> tokenize(String input) {
    ArrayList<String> tokens = new ArrayList<>();
    int index = 0;
    List<String> singleCharTokens = Arrays.asList("(", ")", "*", "/", "+", "-");
    String digitPattern = "\\d|\\.";
    String spacePattern = "\\s";
    while (index < input.length()) {
      if (singleCharTokens.contains(inputAt(input, index))) {
        tokens.add(inputAt(input, index));
        index = index + 1;
      } else if (Pattern.matches(digitPattern, inputAt(input, index))) {
        ArrayList<String> numberList = new ArrayList<>();
        while (index < input.length() && Pattern.matches(digitPattern, inputAt(input, index))) {
          numberList.add(inputAt(input, index));
          index = index + 1;
        }
        tokens.add(join(numberList, ""));
      } else if (Pattern.matches(spacePattern, inputAt(input, index))) {
        index = index + 1;
      } else {
        throw new RuntimeException("Unrecognized token: " + inputAt(input, index));
      }
    }
    return tokens;
  }

  private static String inputAt(String input, int index) {
      return Character.toString(input.charAt(index));
  }

  public static String join(Collection collection, String delimiter) {
    return (String)collection.stream()
            .map(Object::toString)
            .collect(Collectors.joining(delimiter));
  }
}
