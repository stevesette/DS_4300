// ~/code/scala/demo/src/tuples.sc

val tup = (15, "Joe", true, List(1,2,3))

tup._1
tup._2
tup._3
tup._4

val L = List(1,2,3,4,5)

L zip L.map(_ * 2)


