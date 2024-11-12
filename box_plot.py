import csv

def read_csv_data(file_name, column_index=0):
    data_list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) > column_index:
                try:
                    # Extract the value from the desired column and convert it to float
                    data_list.append(float(row[column_index]))
                except ValueError:
                    continue  # Skip rows that cannot be converted to float
    return data_list

def calculate_statistics(data_list):
    data_sorted = sorted(data_list)
    n = len(data_sorted)
    minimum = data_sorted[0]
    maximum = data_sorted[-1]
    if n % 2 == 0:
        median = (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    else:
        median = data_sorted[n // 2]

    q1 = data_sorted[n // 4]
    q3 = data_sorted[(3 * n) // 4]
    iqr = q3 - q1

    return minimum, q1, median, q3, maximum, iqr

file_name = r"C:\Users\rihan\Documents\DM Lab\DM Lab\DM LAB Codes\Box_Plot\auto-mpg.csv"
data_list = read_csv_data(file_name, column_index=2)  # Set index to 2 for Displacement

if data_list:
    minimum, q1, median, q3, maximum, iqr = calculate_statistics(data_list)

    # Print output in the desired format
    print(f"Five number summary for Displacement")
    print(f"Min: {minimum:.2f}")
    print(f"Q1: {q1:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"Max: {maximum:.2f}")
    print(f"IQR: {iqr:.2f}")
else:
    print("No data found in the CSV file.")
