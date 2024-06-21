import slick.jdbc.H2Profile.api._

class FooBar {
  def something(name: String) = {
    val db = Database.forConfig("h2mem1")

    // ruleid: scala-slick-new
    val action = sql"select ID, NAME, AGE from #$name".as[(Int,String,Int)]
    db.run(action)

    // ok: scala-slick-new
    val action2 = sql"select ID, NAME, AGE from $name".as[(Int,String,Int)]
    db.run(action2)
  }
}
