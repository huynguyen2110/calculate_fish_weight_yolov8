from .connect_database import connect_database
from datetime import datetime


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
            'length_carp': row[3],
            'length_tilapia': row[4],
            'length_catfish': row[5],
            'length_perch': row[6],
            'weight_carp': row[7],
            'weight_tilapia': row[8],
            'weight_catfish': row[9],
            'weight_perch': row[10],
            'number_carp': row[11],
            'number_tilapia': row[12],
            'number_catfish': row[13],
            'number_perch': row[14]
        })

    return fishes


def calculate_average_growth(fishes):
    num_fishes = len(fishes)
    if num_fishes < 2:
        return None

    first_date = fishes[0]['created_at']
    last_date = fishes[-1]['created_at']
    num_days = (last_date - first_date).days

    first_weight = float(fishes[0]['weight'])
    last_weight = float(fishes[-1]['weight'])

    average_growth = (last_weight - first_weight) / num_days
    length_carp_average = round((fishes[-1]['length_carp'] - fishes[0]['length_carp']) / num_days, 1)
    length_tilapia_average = round((fishes[-1]['length_tilapia'] - fishes[0]['length_tilapia']) / num_days, 1)
    length_catfish_average = round((fishes[-1]['length_catfish'] - fishes[0]['length_catfish']) / num_days, 1)
    length_perch_average = round((fishes[-1]['length_perch'] - fishes[0]['length_perch']) / num_days, 1)
    weight_carp_average = round((fishes[-1]['weight_carp'] - fishes[0]['weight_carp']) / num_days, 1)
    weight_tilapia_average = round((fishes[-1]['weight_tilapia'] - fishes[0]['weight_tilapia']) / num_days, 1)
    weight_catfish_average = round((fishes[-1]['weight_catfish'] - fishes[0]['weight_catfish']) / num_days, 1)
    weight_perch_average = round((fishes[-1]['weight_perch'] - fishes[0]['weight_perch']) / num_days, 1)

    return [average_growth, length_carp_average, length_tilapia_average, length_catfish_average, length_perch_average,
            weight_carp_average, weight_tilapia_average, weight_catfish_average, weight_perch_average]


def predict_future_weight(target_date):
    target_date = datetime.strptime(target_date, '%Y-%m-%d').date()
    fishes = get_history()
    average_growth, length_carp_average, length_tilapia_average, length_catfish_average, length_perch_average, \
        weight_carp_average, weight_tilapia_average, weight_catfish_average, \
        weight_perch_average = calculate_average_growth(fishes)

    if average_growth is None:
        return None

    last_date = fishes[-1]['created_at']
    num_days = (target_date - last_date).days

    last_weight = float(fishes[-1]['weight'])
    last_length_carp = float(fishes[-1]['length_carp'])
    last_length_tilapia = float(fishes[-1]['length_tilapia'])
    last_length_catfish = float(fishes[-1]['length_catfish'])
    last_length_perch = float(fishes[-1]['length_perch'])
    last_weight_carp = float(fishes[-1]['weight_carp'])
    last_weight_tilapia = float(fishes[-1]['weight_tilapia'])
    last_weight_catfish = float(fishes[-1]['weight_catfish'])
    last_weight_perch = float(fishes[-1]['weight_perch'])

    predicted_weight = last_weight + (average_growth * num_days)
    predicted_length_carp = last_length_carp + (length_carp_average * num_days)
    predicted_length_tilapia = last_length_tilapia + (length_tilapia_average * num_days)
    predicted_length_catfish = last_length_catfish + (length_catfish_average * num_days)
    predicted_length_perch = last_length_perch + (length_perch_average * num_days)
    predicted_weight_carp = last_weight_carp + (weight_carp_average * num_days)
    predicted_weight_tilapia = last_weight_tilapia + (weight_tilapia_average * num_days)
    predicted_weight_catfish = last_weight_catfish + (weight_catfish_average * num_days)
    predicted_weight_perch = last_weight_perch + (weight_perch_average * num_days)

    return [predicted_weight, predicted_length_carp, predicted_length_tilapia, predicted_length_catfish,
            predicted_length_perch, predicted_weight_carp, predicted_weight_tilapia, predicted_weight_catfish,
            predicted_weight_perch]
