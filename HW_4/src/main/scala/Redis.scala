import scala.collection.mutable
import scala.collection.mutable.{HashMap, ListBuffer}

class Redis {
  private val db: HashMap[String, String] = HashMap.empty[String, String]
  private val list_db: HashMap[String, ListBuffer[String]] = HashMap.empty[String, ListBuffer[String]]

  def get(key: String): String = this.db.getOrElse(key, throw new RuntimeException("Key not found"))

  private def list_get_empty(key: String): ListBuffer[String] = this.list_db.getOrElse(key, ListBuffer[String]())

  private def list_get_exception(key: String): ListBuffer[String] = this.list_db.getOrElse(key, throw new RuntimeException("Key not found"))

  def set(key: String, value: String) = this.db += (key -> value)

  def lpush(key: String, value: String) = {
    val newlist = value +: this.list_get_empty(key)
    this.list_db += (key -> newlist)
  }

  def rpush(key: String, value: String) = {
    val newlist = this.list_get_empty(key) :+ value
    this.list_db += (key -> newlist)
  }

  def lpop(key: String): String = this.list_get_exception(key).remove(0)

  def rpop(key: String): String = this.list_get_exception(key).remove(this.list_get_exception(key).length - 1)

  def lrange(key: String, start: Int, stop: Int): ListBuffer[String] = {
    val l = this.list_get_empty(key)
    if (start > l.length || stop > l.length || start > stop) throw new RuntimeException("Index out of bounds")
    else l.slice(start, stop)
  }

  def llen(key: String): Int = this.list_get_empty(key).length

  def flushall = {
    this.db.clear()
    this.list_db.clear()
  }

}

class Graph extends Redis {
  def addNode(v: String) = {
    super.set(v, "exists")
  }

  def addEdge(u: String, v: String) = {
    super.lpush(u, v)
    super.lpush(v, u)
  }

  def adjacent(v: String): ListBuffer[String] = {
    super.lrange(v, 0, super.llen(v))
  }

  def shortestPath(u: String, v: String): ListBuffer[String] = {
    if (super.get(u) != "exists" || super.get(v) != "exists") throw new RuntimeException("Nodes don't exist")
    // doing bfs because why not its easy and since every node is being processed at the same time,
    // the first path to find the target is the shortest (or at least tied for shortest)
    val searchlist = new ListBuffer[String]()
    searchlist += u
    val seenlist = new ListBuffer[String]()
    val path = new mutable.HashMap[String, String]()
    val correct_path = new ListBuffer[String]()
    while (searchlist.nonEmpty) {
      var next = searchlist.remove(0)
      if (next == v) {
        correct_path += next
        while (next != u) {
          next = path.getOrElse(next, throw new RuntimeException("This just shouldn't happen"))
          correct_path += next
        }
      }
      for(s:String <- this.adjacent(next)) {
        if (!seenlist.contains(s)) {
          path += (s -> next)
          searchlist += s
        }
      }
      seenlist += next
    }
    correct_path.reverse
  }
}

object tests extends App {
  // Tests because testing is good
 def test_redis = {
    val db = new Redis()
    db.set("hello", "darkness")
    println(db.get("hello"))
    try {
      db.get("my")
    } catch {
      case _: RuntimeException => println("Exception thrown for missing key")
    }

    db.lpush("song", "darkness")
    db.lpush("song", "hello")
    db.rpush("song", "my")
    db.rpush("song", "old")
    db.rpush("song", "friend")
    db.lrange("song", 0, 5).foreach { x: String => print(x + " ") }
    print("\n")

    println(db.lpop("song") + " " + db.rpop("song"))
    try {
      db.rpop("hello")
    } catch {
      case _: RuntimeException => println("Exception thrown for missing key")
    }

    println(db.llen("song"))
    println(db.llen("hello"))

    db.flushall
    println(db.llen("song"))
    try {
      db.rpop("hello")
    } catch {
      case _: RuntimeException => println("Exception thrown for missing key")
    }
    try {
      db.get("my")
    } catch {
      case _: RuntimeException => println("Exception thrown for missing key")
    }
  }

  def test_graph = {
    val gdb = new Graph()
    gdb.addNode("x")
    gdb.addNode("j")
    gdb.addNode("f")
    gdb.addNode("r")
    gdb.addNode("b")
    gdb.addNode("c")
    gdb.addNode("e")
    gdb.addNode("y")
    gdb.addEdge("x", "j")

    gdb.addEdge("j", "f")
    gdb.addEdge("j", "b")
    gdb.addEdge("j", "r")

    gdb.addEdge("f", "b")
    gdb.addEdge("f", "e")

    gdb.addEdge("r", "y")
    gdb.addEdge("r", "e")
    gdb.addEdge("r", "c")

    gdb.addEdge("b", "c")

    println(gdb.shortestPath("x", "y"))
  }
  test_graph
}