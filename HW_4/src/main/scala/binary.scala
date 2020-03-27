import breeze.linalg._
import breeze.plot._

object Binary extends App {
  def toBinary(x: Int, bits: Int): String = {
    if (x==0)
      "0" * bits
    else if (x == 1)
      "0" * (bits-1) + "1"
    else toBinary(x / 2, bits - 1) + (x % 2).toString()
  }
  println(toBinary(1234567890, 32))
  def weight(b: String): Int = b.count((_ == '1'))
  val bin = toBinary(37, 8)
  print(weight(bin))

  val f = Figure()
  val p = f.subplot(0)
  val x = linspace(0.0,1024.0)
  p += plot(x, weight(toBinary(x, 2)))
  p.xlabel = "x axis"
  p.ylabel = "y axis"
  f.saveas("weights.png")
  val weights_and_binaries = (0 to 1024).map(x=>(x,toBinary(x,2))).map{case (x, y)=> (x, weight(y))}
}


