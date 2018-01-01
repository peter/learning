package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if (c < 0 || c > r || r < 0) {
        // Outside the triangle
        0
      } else if (c == 0 || c == r) {
        // Edges of triangle are always 1. There are r + 1 columns.
        1
      } else {
        // Inner digit in triangle is sum of left and right column of previous row
        pascal(c - 1, r - 1) + pascal(c, r - 1)
      }
    }

  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def isBalanced(chars: List[Char], nOpen: Int): Boolean = {
        if (nOpen < 0) {
          false
        } else if (chars.isEmpty) {
          nOpen == 0
        } else if (chars.head == '(') {
          isBalanced(chars.tail, nOpen + 1)
        } else if (chars.head == ')') {
          isBalanced(chars.tail, nOpen - 1)
        } else {
          isBalanced(chars.tail, nOpen)
        }
      }
      isBalanced(chars, 0)
    }

  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      def findPermutations(money: Int, coins: List[Int]): List[List[Int]] = {
        coins.filter { _ <= money }.flatMap { coin =>
          val permutations = findPermutations(money - coin, coins).map { coin :: _ }
          if (permutations.isEmpty) List(List(coin)) else permutations
        }
      }
      def findDistinctPermutations(money: Int, coins: List[Int]): List[List[Int]] = {
        findPermutations(money, coins).map { _.sorted }.distinct
      }
      findDistinctPermutations(money, coins).length
    }
  }
