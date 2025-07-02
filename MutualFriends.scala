// Fonction pour générer les couples triés
def pairs(str: Array[String]) = {
  val user = str(0)
  val friends = str(1).split(",")
  for (friend <- friends) yield {
    val pair = if (user.toInt < friend.toInt) (user, friend) else (friend, user)
    (pair, friends)
  }
}

// Charger les données depuis sample.txt
val data = sc.textFile("sample.txt")
val data1 = data.map(_.split("\t")).filter(x => x.length == 2)
val pairCounts = data1.flatMap(pairs).reduceByKey((a, b) => a.intersect(b))

// Formater le résultat
val p1 = pairCounts.map {
  case ((u1, u2), common) => s"$u1\t$u2\t${common.mkString(",")}"
}

// Sauvegarder résultat global
p1.saveAsTextFile("output")

// Extraire les résultats spécifiques
var ans = ""
val queries = Seq(("0", "4"), ("20", "22939"), ("1", "29826"), ("19272", "6222"), ("28041", "28056"))

for ((u1, u2) <- queries) {
  val result = p1.map(_.split("\t"))
    .filter(x => x.length == 3 && x(0) == u1 && x(1) == u2)
    .flatMap(x => x(2).split(",")).collect()

  ans += s"$u1\t$u2\t${result.mkString(",")}\n"
}

val answer = sc.parallelize(Seq(ans))
answer.saveAsTextFile("output1")
