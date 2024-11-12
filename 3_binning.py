# import csv

# def main():
#     input_filename = r'C:\Users\rihan\Documents\DM Lab\DM Lab\DM LAB Codes\3_Binning\auto-mpg.csv'
    
#     with open(input_filename, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         data = [float(row[headers.index('AnnualIncome')]) for row in reader]
#         data.sort()

#     num_bins = int(input('Enter the number of bins: '))
#     total_elements = len(data)
#     bin_size = total_elements // num_bins + (total_elements % num_bins > 0)

#     bins = [data[i:i + bin_size] for i in range(0, total_elements, bin_size)]

#     for i, bin in enumerate(bins):
#         print(f"\nBin {i + 1}: {bin}\n")

#         mean_value = sum(bin) / len(bin)
#         smooth_by_mean = [round(mean_value)] * len(bin)
#         print(f"Smoothing by Mean:\n{', '.join(map(str, smooth_by_mean))}")

#         sorted_bin = sorted(bin)
#         median_value = sorted_bin[len(sorted_bin) // 2]
#         smooth_by_median = [median_value] * len(bin)
#         print(f"Smoothing by Median:\n{', '.join(map(str, smooth_by_median))}")

#         min_val = min(bin)
#         max_val = max(bin)
#         smooth_by_boundary = [
#             min_val if abs(val - min_val) < abs(val - max_val) else max_val for val in bin
#         ]
#         print(f"Smoothing by Boundary:\n{', '.join(map(str, smooth_by_boundary))}\n")


# if __name__ == '__main__':
#     main()

import csv

def main():
    input_filename = r'C:\Users\rihan\Documents\DM Lab\DM Lab\DM LAB Codes\3_Binning\auto-mpg.csv'
    
    with open(input_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        # Use the 'MPG' column for data extraction
        data = [float(row[headers.index('MPG')]) for row in reader]
        data.sort()

    num_bins = int(input('Enter the number of bins: '))
    total_elements = len(data)
    bin_size = total_elements // num_bins + (total_elements % num_bins > 0)

    bins = [data[i:i + bin_size] for i in range(0, total_elements, bin_size)]

    for i, bin in enumerate(bins):
        print(f"\nBin {i + 1}: {bin}\n")

        mean_value = sum(bin) / len(bin)
        smooth_by_mean = [round(mean_value)] * len(bin)
        print(f"Smoothing by Mean:\n{', '.join(map(str, smooth_by_mean))}")

        sorted_bin = sorted(bin)
        median_value = sorted_bin[len(sorted_bin) // 2]
        smooth_by_median = [median_value] * len(bin)
        print(f"Smoothing by Median:\n{', '.join(map(str, smooth_by_median))}")

        min_val = min(bin)
        max_val = max(bin)
        smooth_by_boundary = [
            min_val if abs(val - min_val) < abs(val - max_val) else max_val for val in bin
        ]
        print(f"Smoothing by Boundary:\n{', '.join(map(str, smooth_by_boundary))}\n")


if __name__ == '__main__':
    main()

