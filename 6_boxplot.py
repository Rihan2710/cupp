import csv

filename = 'financial_risk_analysis.csv'
loan_amounts = []

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        loan_amounts.append(float(row['LoanAmount']))
sorted_loan_amounts = sorted(loan_amounts)

def calculate_quartiles(data):
    data.sort()
    n = len(data)
    
    def get_quartile_position(n, frac):
        pos = (n-1) * frac
        if pos.is_integer():
            return data[int(pos)]
        else:
            l = int(pos)
            h = l + 1
            return (data[l] + data[h]) / 2

    Q1 = get_quartile_position(n, 0.25)
    Q3 = get_quartile_position(n, 0.75)
    
    return Q1, Q3


def calculate_median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]
    
    
median = calculate_median(sorted_loan_amounts)
Q1, Q3 = calculate_quartiles(sorted_loan_amounts)
min_val = min(sorted_loan_amounts)
max_val = max(sorted_loan_amounts)
print("\nFive number summary for Loan amounts\n")
print(f"Min: {min_val:.2f}\nQ1: {Q1:.2f}\nMedian: {median:.2f}\nQ3: {Q3:.2f}\nMax: {max_val:.2f}\nIQR: {Q3-Q1 :.2f}\n")
