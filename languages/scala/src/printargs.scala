var i = 0
while (i < args.length) {
  println(args(i))
  i += 1
}

args.foreach { arg => println(arg) }

args.foreach { println(_) }

args.foreach(println)

for(arg <- args)
  println(arg)
