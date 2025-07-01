# Analyse des amis communs avec PySpark

## Objectif  
Ce projet implémente un programme **PySpark** permettant de trouver les **amis communs entre deux utilisateurs** (**Sidi** et **Mohamed**) dans un graphe social représenté par un fichier texte.  
Il utilise les **RDDs de Spark** pour un traitement distribué et efficace des données.

---

## Jeu de données

Le fichier d’entrée `data.txt` suit le format suivant :

```

\<user\_id> <Nom> \<id\_ami1>,\<id\_ami2>,...

```

### Exemple :

```

1	Sidi	2,3,4
2	Mohamed	1,3,5
3	Aicha	1,2,4,6
4	Ahmed	1,3
5	Leila	2
6	Issa	3

````

Chaque ligne représente un utilisateur avec :
-  Son **identifiant** (`user_id`)
-  Son **nom**
-  Une liste d'amis (`friend_id`) séparés par des virgules

>  **Les relations d’amitié sont considérées comme mutuelles.**

---

##  Prérequis

- [ ] Apache Spark **3.4.x**
- [ ] Python **3.9.x**
- [ ] Bibliothèque **PySpark**
- [ ] Java **8**

---

## ⚙️ Installation et exécution

### 1. Installer Spark

- Télécharger Spark : [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)
- Définir les variables d’environnement :
  ```bash
  export SPARK_HOME=/chemin/vers/spark
  export PATH=$SPARK_HOME/bin:$PATH
````

* Installer PySpark :

  ```bash
  pip install pyspark
  ```

### 2. Préparer le fichier d’entrée

* Placer le fichier `data.txt` dans le répertoire du projet.

### 3. Lancer le programme

* Enregistrer le fichier Python sous le nom `mutual_friends.py`
* Exécuter avec Spark :

```bash
spark-submit mutual_friends.py
```

---

## Étapes d’exécution

1. **Chargement des données** : Lecture du fichier `data.txt` en RDD
2. **Parsing** : Extraction des champs `ID`, `Nom`, `Liste d’amis`
3. **Génération des paires** : Création des paires `(min(ID1, ID2), max(ID1, ID2))`
4. **Intersection** : Calcul de la liste des amis communs entre chaque paire
5. **Filtrage** : Extraction spécifique de la paire `(1, 2)` → **Sidi & Mohamed**
6. **Affichage** : Résultat écrit dans le fichier `test_output.txt` au format :

```text
Ami(s) commun(s) entre 1<Sidi> et 2<Mohamed> : Aicha
```

---

## Exemple de sortie

Pour le jeu de données fourni :

```text
Ami(s) commun(s) entre 1<Sidi> et 2<Mohamed> : Aicha
```

Cela signifie que **Aicha** est **amie à la fois avec Sidi et Mohamed**.

---
##  Remarques

* Le script suppose que les amitiés sont **bidirectionnelles**.
* Les identifiants sont traités sous forme de **chaînes de caractères (string)**.
* Le script est optimisé pour les petits à moyens jeux de données.
* Le chemin vers le fichier doit être **correctement configuré** dans le code (`file:///...`).

---
