from pyspark import SparkContext

def parse_line_safe(line):
    try:
        if line.startswith("#") or not line.strip():
            return None
        parts = line.strip().split("\t")
        if len(parts) != 3:
            return None
        user_id = parts[0].strip()
        name = parts[1].strip()
        friends = parts[2].split(",")
        return (user_id, name, [f.strip() for f in friends if f.strip()])
    except Exception:
        return None

# 🔁 Création symétrique des paires (pour chaque ami, on émet la paire)
def make_symmetric_pairs(record):
    user_id, _, friends = record
    result = []
    for friend in friends:
        key = tuple(sorted([user_id, friend]))  # (min, max)
        result.append((key, set(friends)))
    return result

def main():
    sc = SparkContext(appName="MutualFriends")
    
    lines = sc.textFile("file:///home/daouda/tp2/data.txt")
    
    parsed = lines.map(parse_line_safe).filter(lambda x: x is not None)
    
    id_to_name = parsed.map(lambda x: (x[0], x[1])).collectAsMap()
    
    # Générer les paires symétriques
    pairs = parsed.flatMap(make_symmetric_pairs)

    # Faire intersection
    mutual = pairs.reduceByKey(lambda x, y: x & y)

    target = tuple(sorted(["1", "2"]))  # Mohamed & Sidi
    result = mutual.filter(lambda x: x[0] == target).collect()

    with open("test_output.txt", "w") as f:
        if result and result[0][1]:
            names = [id_to_name.get(fid, fid) for fid in sorted(result[0][1])]
            f.write(f"Ami(s) commun(s) entre {target[0]}<{id_to_name[target[0]]}> et {target[1]}<{id_to_name[target[1]]}> : {', '.join(names)}\n")
        else:
            f.write("Aucun ami commun trouvé.\n")

    sc.stop()

if __name__ == "__main__":
    main()

