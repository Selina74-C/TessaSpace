import csv
import os

def get_tidal_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'retail-trade-survey-june-2025-quarter.csv')
    data_values = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                value = float(row['Data_value'])
                data_values.append(value)
            except (ValueError, KeyError):
                continue
    # Normalize data for visualization (0-1)
    if data_values:
        min_val = min(data_values)
        max_val = max(data_values)
        norm = [(v - min_val) / (max_val - min_val) if max_val > min_val else 0 for v in data_values]
        return norm
    return []
