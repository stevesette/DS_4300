object Partition extends App {
  def moved(records: Int, startN: Int, endN: Int): Double = {
    return (0 to (records - 1) ).map(x => (x % startN, x % endN))
      .map{case (x, y) => x - y}.map(x => if (x == 0) 0 else 1).sum
  }

  println(moved(1000000, 100, 107))
}