package main.scala

import breeze.plot_


object Binary extends App {
  def toBinary(x: Int, bits: Int): String = {
    if (x==0)
      "0" * bits
    else if (x == 1)
      "0" * (bits-1) + "1"
    else toBinary(x / 2, bits - 1) + (x % 2).toString()
  }

  def weight(b: String): Int = b.count((_ == '1'))
  val bin = toBinary(37, 8)
  print(weight(bin))
}


