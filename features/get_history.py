from .connect_database import connect_database


def get_history():
    db = connect_database()

    query = "SELECT * FROM history LIMIT 20"

    cursor = db.cursor()
    cursor.execute(query)

    fishes = []
    for row in cursor.fetchall():
        fishes.append({
            'id': row[0],
            'weight': row[1],
            'created_at': row[2],
            'number_carp': row[3],
            'number_tilapia': row[4],
            'number_catfish': row[5],
            'number_perch': row[6],
            'length_carp': row[7],
            'length_tilapia': row[8],
            'length_catfish': row[9],
            'length_perch': row[10],
            'weight_carp': row[11],
            'weight_tilapia': row[12],
            'weight_catfish': row[13],
            'weight_perch': row[14]
        })

    return fishes
