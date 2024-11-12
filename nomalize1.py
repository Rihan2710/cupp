import csv

def minmax(data, new_min=0, new_max=1):
    min_val = min(data)
    max_val = max(data)
    minmax_normal = [((x - min_val) * (new_max - new_min) / (max_val - min_val) + new_min) for x in data]
    return minmax_normal

def zscore(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    zscore_normal = [(x - mean) / std_dev for x in data]
    return zscore_normal

def read_csv_data(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  
        columns = {header: [] for header in headers}  
        for row in csv_reader:
            for i, value in enumerate(row):
                try:
                    columns[headers[i]].append(float(value))  
                except ValueError:
                    columns[headers[i]].append(None) 
    return headers, columns

def write_csv_data(file_path, headers, normalized_columns):
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)  
        for i in range(len(normalized_columns[headers[0]])): 
            row = [normalized_columns[header][i] for header in headers]  
            csv_writer.writerow(row)

def normalize_and_save(file_path, min_max_output, z_score_output):
    headers, columns = read_csv_data(file_path)
    min_max_columns = {header: [] for header in headers}
    z_score_columns = {header: [] for header in headers}
    for header in headers:
        col_data = columns[header]
        numeric_data = [x for x in col_data if x is not None]
        if numeric_data:  
            min_max_minmax_normal = minmax(numeric_data)
            z_score_zscore_normal = zscore(numeric_data)
            min_max_columns[header] = [min_max_minmax_normal.pop(0) if val is not None else None for val in col_data]
            z_score_columns[header] = [z_score_zscore_normal.pop(0) if val is not None else None for val in col_data]        
        else:
            min_max_columns[header] = col_data 
            z_score_columns[header] = col_data
    write_csv_data(min_max_output, headers, min_max_columns)
    write_csv_data(z_score_output, headers, z_score_columns)

ipfile = 'C:\\Users\\rihan\\Documents\\PYTHON\\Normalization\\Folds5x2_pp.csv'
minmax_op = 'C:\\Users\\rihan\\Documents\\PYTHON\\Normalization\\min-maxop.csv'
zscore_op = 'C:\\Users\\rihan\\Documents\\PYTHON\\Normalization\\z-score.csv'
  
normalize_and_save(ipfile, minmax_op, zscore_op)
print(f"Min-max scaling saved to {minmax_op}")
print(f"Z-score normalization saved to {zscore_op}")