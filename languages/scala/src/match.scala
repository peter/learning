val firstArg = if (args.length > 0) args(0) else ""
val friend =
  firstArg match {
    case "salt" => "pepper"
    case "chips" => "salsa"
    case _ => "huh?"
  }
println(friend)
