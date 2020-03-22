// Chapter 2: Numbers

Short.MinValue
Short.MaxValue
Int.MinValue
Int.MaxValue


import java.time
import java.time.LocalDateTime

LocalDateTime.now

// 2.1 Parsing

"100".toInt
"100.4".toDouble

val a = 1000L
val b = 1000: Long
val c: Long = 1000


def ~=(x: Double, y: Double, precision: Double) = {
  if ((x-y).abs < precision) true else false
}

val x = 0.3
val y = .1 + .2

~=(x,y,0.001)


// 2.7 Random numbers

val r = scala.util.Random

r.nextInt
r.nextInt(100)
r.nextFloat
r.nextDouble

r.nextPrintableChar
r.nextPrintableChar
val pw = for (i <- 0 to 10)
  yield r.nextPrintableChar()

pw.mkString("")

for (i <- 1 to 10 by 2)
  println(i)

(1 to 10).toList
