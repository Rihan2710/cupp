import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
def calculate_and_display_weights(data):
    headers = data[0].keys()
    numeric_headers = [header for header in headers if header != 'Class']

    totals = {header: sum(int(row[header]) for row in data) for header in numeric_headers}

    #column width
    class_width = 12
    data_width = 10
    dwt_width = 12
    twt_width = 12
    total_width = 8

    #spacing
    print(f"\n{'Class':<{class_width}} " + " ".join([f"{header:<{data_width}} {'d-wt ' + header:<{dwt_width}} {'t-wt ' + header:<{twt_width}}" for header in numeric_headers]) + f"{'Total':<{total_width}}")
    print("-" * (class_width + len(numeric_headers) * (data_width + dwt_width + twt_width) + total_width))

    total_dwt = {header: 0 for header in numeric_headers}
    total_twt = {header: 0 for header in numeric_headers}

    for row in data:
        category = row['Class']
        total = sum(int(row[header]) for header in numeric_headers)

        dwt = {header: (int(row[header]) / totals[header]) * 100 if totals[header] > 0 else 0 for header in numeric_headers}
        twt = {header: (int(row[header]) / total) * 100 if total > 0 else 0 for header in numeric_headers}

        for header in numeric_headers:
            total_dwt[header] += dwt[header]
            total_twt[header] += twt[header]

        print(f"{category:<{class_width}} " + " ".join([f"{row[header]:<{data_width}} {dwt[header]:<{dwt_width}.2f} {twt[header]:<{twt_width}.2f}" for header in numeric_headers]) + f" {total:<{total_width}}")

    overall_twt = {header: totals[header] / sum(totals.values()) * 100 for header in numeric_headers}
    final_total = sum(totals.values())

    print("-" * (class_width + len(numeric_headers) * (data_width + dwt_width + twt_width) + total_width))
    print(f"{'Total':<{class_width}} " + " ".join([f"{totals[header]:<{data_width}} {total_dwt[header]:<{dwt_width}.2f} {overall_twt[header]:<{twt_width}.2f}" for header in numeric_headers]) + f" {final_total:<{total_width}}\n")

filename = r'C:\Users\rihan\Documents\DM Lab\DM Lab\DM LAB Codes\5_td_weight\t_d_data.csv'

data = read_csv(filename)
calculate_and_display_weights(data)
