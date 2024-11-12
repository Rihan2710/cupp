import csv

def load_dataset(filename):
    with open(filename, 'r') as file:
        dataset = list(csv.reader(file))
        return [[float(x) for x in row] for row in dataset[1:]]

def linear_regression_coefficients(X, y):
    n = len(X)
    x_mean = sum(X) / n
    y_mean = sum(y) / n
    numerator = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((X[i] - x_mean) ** 2 for i in range(n))
    m = numerator / denominator
    c = y_mean - m * x_mean
    return c, m

def main():
    filename = 'car_data.csv'
    dataset = load_dataset(filename)
    X = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    c, m = linear_regression_coefficients(X, y)
    print(f"Linear Regression Coefficient:\n\tIntercept (c): {c:0.3f}\n\tSlope (m): {m:0.3f}")
    print(f"\nEquation of y = {m:0.3f}x + {c:0.3f}")

if __name__ == "__main__":
    main()
