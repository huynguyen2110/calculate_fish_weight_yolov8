from features.connect_database import connect_database
from datetime import date


def insert_into_database(total_weight, number_fish_specific):
    if number_fish_specific['carp']['number'] != 0:
        length_carp = round(number_fish_specific['carp']['length'] / number_fish_specific['carp']['number'], 1)
        weight_carp = round(number_fish_specific['carp']['weight'] / number_fish_specific['carp']['number'], 1)
    else:
        length_carp = 0
        weight_carp = 0

    if number_fish_specific['tilapia']['number'] != 0:
        length_tilapia = round(number_fish_specific['tilapia']['length'] / number_fish_specific['tilapia']['number'], 1)
        weight_tilapia = round(number_fish_specific['tilapia']['weight'] / number_fish_specific['tilapia']['number'], 1)
    else:
        length_tilapia = 0
        weight_tilapia = 0

    if number_fish_specific['catfish']['number'] != 0:
        print(round(number_fish_specific['catfish']['weight'] / number_fish_specific['catfish']['number'], 3))
        length_catfish = round(number_fish_specific['catfish']['length'] / number_fish_specific['catfish']['number'], 1)
        weight_catfish = round(number_fish_specific['catfish']['weight'] / number_fish_specific['catfish']['number'], 1)
    else:
        length_catfish = 0
        weight_catfish = 0

    if number_fish_specific['perch']['number'] != 0:
        length_perch = round(number_fish_specific['perch']['length'] / number_fish_specific['perch']['number'], 1)
        weight_perch = round(number_fish_specific['perch']['weight'] / number_fish_specific['perch']['number'], 1)
    else:
        length_perch = 0
        weight_perch = 0
    db = connect_database()
    query = "INSERT INTO history (weight, created_at, " \
            "number_carp, number_tilapia, number_catfish, number_perch, " \
            "length_carp, length_tilapia, length_catfish, length_perch, " \
            "weight_carp, weight_tilapia, weight_catfish, weight_perch) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        total_weight, date.today(), number_fish_specific['carp']['number'], number_fish_specific['tilapia']['number'],
        number_fish_specific['catfish']['number'], number_fish_specific['perch']['number'], length_carp, length_tilapia,
        length_catfish, length_perch, weight_carp, weight_tilapia, weight_catfish, weight_perch)

    db.cursor().execute(query, values)
    db.commit()
