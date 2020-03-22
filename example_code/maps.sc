// Maps

val m = Map("a"->1, "b"->2, "c"->3)

m("b")

val n = m + ("d"->4)

m.toList

val tup = ("a", 1)
tup._1
tup._2

m.map(_._1)
m.map(_._2).reduce((x,y) => x + y)

val L = 1::2::3::4::5::6::7::8::9::10::Nil

def square(x:Int):Int = x*x
def cube(x:Int):Int = x*x
def double(x:Int) = 2*x

val f = Map[String, Int=>Int]("s"->square, "c"->cube, "d"->double)

f("s")(5)

L.map(f("d"))


m.getOrElse("x", 99)

