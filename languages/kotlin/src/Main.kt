
fun main(args : Array<String>) {
    println("Hello, world!")

    val numberString1 = "1,2,3,4,5"
    val numbers: List<Int> = numberString1.split(",").map { it.toInt() }
    println(numbers)

    val numberList = listOf(4, 8, 15, 16, 23, 42)
    val numberString = numberList.joinToString(",")
    println(numberString)
}
