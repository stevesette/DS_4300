package cookbook.objects


object CashRegister {
  def open { println("opened") }
  def close { println("closed") }
}


object Singleton extends App {
  CashRegister.open
  CashRegister.close
}
