import scala.io._


/**
  * Count the number of null-values in each column of a .CSV
  */
object CountingNullValues {

  def main(args: Array[String]): Unit = {


    val filename = "/Users/rachlin/data/weather/stations.csv"

    // METHOD 1
    // This is a straight-forward approach using two inner loops
    // But it assumes you know in advance the number of columns on your input
    // You could fix that!

    val nulls = Array[Int](0, 0, 0, 0)
    for (line <- Source.fromFile(filename).getLines) {
      val toks = line.split(",", -1)
      for (i <- 0 until toks.length)
        if (toks(i) == "") nulls(i) = nulls(i) + 1
    }
    println(nulls.mkString(","))


    // METHOD 2
    // This uses a var to incrementally add null counts to each row
    // Basically nulls2 is serving as a multi-column null counter
    var nulls2 = Array[Int](0, 0, 0, 0)
    for (line <- Source.fromFile(filename).getLines)
      nulls2 = (nulls2 zip line.split(",", -1).map(z => if (z == "") 1 else 0)).map { case (x, y) => x + y }
    println(nulls2.mkString(","))


    // METHOD 3
    // Whoa this looks intimidating.  But break it down in the scala REPL and it isn't so bad.
    // The count was one line of chained together commands using a map and a reduce.
    // It shows the power of functional programming but is admittedly harder to understand.

    val nulls3 = Source.fromFile(filename).getLines
      .map(_.split(",", -1)).map(a => a.map(z => if (z == "") 1 else 0))
      .reduce((x, y) => (x zip y).map { case (u, v) => u + v })

    println(nulls3.mkString(","))

  }
}



