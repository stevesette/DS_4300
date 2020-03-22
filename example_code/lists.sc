// ~/code/scala/demo/src/lists.sc

val L = List(19,3,14,5,99,8,64,32,11)

L.length

L(3)

L.head
L.tail
L.reverse
L.take(4)
L.drop(4)

L.isEmpty
L.contains(14)
L.filter((x:Int)=>x>50)
L.filter((x)=>x>50)
L.filter(_>50)

L.splitAt(L.length / 2)


L.map(x => x * 2)
L.map(_ * 2)


def g(x: Int): Int = x*x

g(3)

L.map(g)


L zip L.map(g)


L.reduce(_ + _)

L.reduce((x,y)=>Math.max(x,y))
L.reduce(Math.max(_,_))




Range(1, 100).reduce(_+_)



val M = "hello" :: "world" :: "how" :: "are" :: "you" :: Nil

val lol = List(List(1,2,3), List(4,5,6), List(7,8,9, 10))

lol(2)
lol.flatten










