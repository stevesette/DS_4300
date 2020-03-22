package cookbook.objects

class Pizza (var crustType: String) {
  override def toString = "Crust type is " + crustType
}

// companion object
object Pizza {
  val CRUST_TYPE_THIN = "thin"
  val CRUST_TYPE_THICK = "thick"
  def getFoo = "Foo"
}


object Main extends App {


  println(Pizza.CRUST_TYPE_THIN)
  println(Pizza.getFoo)

  var p = new Pizza(Pizza.CRUST_TYPE_THICK)
  println(p)

}