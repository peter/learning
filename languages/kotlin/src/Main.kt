
import java.util.Arrays

fun main(args : Array<String>) {
    println("Hello, world!")

    val numberString = "1,2,3,4,5"
    val numbers: List<Int> = numberString.split(",").map { it.toInt() }
    println(numbers)
}
