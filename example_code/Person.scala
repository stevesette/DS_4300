package cookbook.classes

class Person(var firstName: String, var lastName: String, var age: Int = 40) {

  // This is an auxiliary constructor
  def this(lastName: String) {  // it has a different sig
    this("", lastName)          // it uses this to call the main constructor
  }

  println(s"the constructor for $lastName begins")

  // some class fields
  private val HOME = System.getProperty("user.home")

  var address = None: Option[Address]


  // some methods
  override def toString = s"$firstName $lastName is $age years old and lives in ${address}"
  def printHome { println(s"HOME = $HOME") }
  def printFullName { println(this) }  // uses toString
  def printAddress: Unit = {
    address.foreach { a => println(s"${a.city} ${a.state} ${a.zip} ")}
  }

  printHome
  printFullName
  printAddress
  println(s"still in the $lastName constructor")

}



case class Address(city: String, state: String, zip: String)



// Singleton objects (using private keyword)
class Brain private {
  override def toString = "This is the brain."
}

object Brain {
  val brain = new Brain
  def getInstance = brain
}

object Test extends App {

  val p = new Person("John", "Doe")
  p.firstName = "Jane"
  p.age = 30
  println(p.toString)
  p.address = Some(Address("Boston", "MA", "02115"))
  p.printAddress

  val q = new Person("Smith")


  val b = Brain.getInstance
  println(b)


}