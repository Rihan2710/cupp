import csv

class_names = []
india_counts = []
usa_counts = []


with open(r'C:\Users\rihan\Documents\PYTHON\t_d_data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        class_names.append(row[0])
        india_counts.append(int(row[1]))
        usa_counts.append(int(row[2]))

total_india_count = sum(india_counts)
total_usa_count = sum(usa_counts)

total_counts = [india_counts[i] + usa_counts[i] for i in range(len(class_names))]

# Calculate t and d weights
india_t_weights = [(count / total_counts[i]) * 100 for i, count in enumerate(india_counts)]
usa_t_weights = [(count / total_counts[i]) * 100 for i, count in enumerate(usa_counts)]

india_d_weights = [(india_counts[i] / total_india_count) * 100 for i in range(len(class_names))]
usa_d_weights = [(usa_counts[i] / total_usa_count) * 100 for i in range(len(class_names))]

print(f"{'Class':<12} | {'India Count':<12} | {'India t-weight (%)':<17} | {'India d-weight (%)':<17} | "f"{'USA Count':<12} | {'USA t-weight (%)':<17} | {'USA d-weight (%)':<17} | "
      f"{'Total Count':<12} | {'Total t-weight (%)':<17} | {'Total d-weight (%)'}")

print('-' * 130)

for i in range(len(class_names)):
    print(f"{class_names[i]:<12} | {india_counts[i]:<12} | {india_t_weights[i]:<17.2f} | {india_d_weights[i]:<17.2f} | "
          f"{usa_counts[i]:<12} | {usa_t_weights[i]:<17.2f} | {usa_d_weights[i]:<17.2f} | "
          f"{total_counts[i]:<12} | {india_t_weights[i] + usa_t_weights[i]:<17.2f} | {india_d_weights[i] + usa_d_weights[i]:<17.2f}")
