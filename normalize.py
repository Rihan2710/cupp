
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

def write_csv_with_input_output(file_path, headers, input_columns, min_max_columns, z_score_columns):
    new_headers = []
    for header in headers:
        new_headers.append(f"{header} (Input)")
        new_headers.append(f"{header} (Min-Max Output)")
        new_headers.append(f"{header} (Z-Score Output)")

    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(new_headers)

        for i in range(len(input_columns[headers[0]])):
            row = []
            for header in headers:
                row.append(input_columns[header][i])
                row.append(min_max_columns[header][i])
                row.append(z_score_columns[header][i])  
            csv_writer.writerow(row)

def normalize_and_save(file_path, output_file):

    new_min = float(input("Enter the new minimum value for Min-Max normalization: "))
    new_max = float(input("Enter the new maximum value for Min-Max normalization: "))
    
    headers, columns = read_csv_data(file_path)
    min_max_columns = {header: [] for header in headers}
    z_score_columns = {header: [] for header in headers}
    
    for header in headers:
        col_data = columns[header]
        numeric_data = [x for x in col_data if x is not None]
        if numeric_data:
            min_max_normal = minmax(numeric_data, new_min, new_max)
            z_score_normal = zscore(numeric_data)
            min_max_columns[header] = [min_max_normal.pop(0) if val is not None else None for val in col_data]
            z_score_columns[header] = [z_score_normal.pop(0) if val is not None else None for val in col_data]
        else:
            min_max_columns[header] = col_data
            z_score_columns[header] = col_data
    
    write_csv_with_input_output(output_file, headers, columns, min_max_columns, z_score_columns)

ipfile = r'C:\Users\rihan\Documents\DM Lab\DM Lab\DM LAB Codes\2.0_Normalization\auto-mpg.csv'
output_file = r'C:\Users\rihan\Documents\PYTHON\Normalization\normalized_output.csv'

normalize_and_save(ipfile, output_file)

print(f"Normalization (Min-Max and Z-Score) saved with input and output to {output_file}")
