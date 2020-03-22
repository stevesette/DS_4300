object HelloWorldWithMain {

  def main(args: Array[String]): Unit = {

    println("Here are the arguments")

    // Loop over the arguments
    for (i <- 0 to args.length - 1)
      println(args(i))


    // Better
    for (i <- 0 until args.length)
      println(args(i))


    for (i <- args.indices)
      println(args(i))


    // Better
    for (arg <- args)
      println(arg)

    // Better
    args.foreach((s: String) => println(s))

    // Even better
    args.foreach((s) => println(s))

    // Even better
    args.foreach(s => println(s))

    // Even better
    args.foreach(println(_))

    // Even better
    args.foreach(println)

  }

}
