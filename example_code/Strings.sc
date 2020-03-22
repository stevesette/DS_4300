
// String operations
val s = "Hello World"

s.getClass.getName
s.length

val s2 = "John" + " " + "Doe"

// seq of chars
s.foreach(println)

for (c <- s) println(c)

s.getBytes.foreach(println)

val result = s.filter(_ != 'l')

"abcde".combinations(3).toList

"scala".drop(2)
"scala".drop(2).take(2)
"scala".drop(2).take(2).capitalize


  // 1.1 Equality

val st1 = "Hello"
val st2 = "Hello"
val st3 = "H"+"ello"
val st4 = null // not idiomatic Scala.  Use Option instead

val b1 = st1 == st2
val b2 = st1 == st3
val b3 = st1 == st4

"john".equalsIgnoreCase("John")

// 1.2 multiline
val foo =
  """This is
    |a converted multiline
    |string which can contain "quoted" or 'quoted' strings
  """.stripMargin

foo.replaceAll("\n"," ")

// 1.3 Splitting
"hello world".split(" ")

"this is a test".split(" ").foreach(println)

"a,b,c,d,,".split(",",-1)

"a  \t b    c d   e   ".split("\\s+")



// 1.4 interpolation
val name = "Fred"
val age = 33
val weight = 200.0
println(s"$name is $age years old and weights $weight lbs.")

println(s"Age next year: ${age + 1}")

case class Student(name: String, score: Int)
val hannah = Student("Hanna", 95)
println(s"${hannah.name} scored a ${hannah.score}\n")


// 1.5 processing one char at a time
val upper1 = "hello world".map(c => c.toUpper)
val upper2 = "hello world".map(_.toUpper)

val upper3 = for (c <- "hello world")
  yield c.toUpper

// 1.6-1.9 patterns
val address = "123 Main St Suite 101"
val pattern = "[0-9]+".r

pattern.findAllIn(address).toList
pattern.replaceAllIn(address, "[REDACTED]")


val pattern2 = "([0-9]+) ([A-Za-z]+)".r
val pattern2(count,fruit) = "100 Bananas"

"abcdef".charAt(2)




