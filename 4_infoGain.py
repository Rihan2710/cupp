import csv
import math

# Function to calculate entropy
def calculate_entropy(y):
    label_counts = {}
    for label in y:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    total_count = len(y)
    entropy = 0.0
    for count in label_counts.values():
        probability = count / total_count
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

# Function to calculate information gain for a specific feature
def calculate_information_gain(X, y, feature_index):
    original_entropy = calculate_entropy(y)
    feature_values = {}
    for i in range(len(X)):
        feature_value = X[i][feature_index]
        if feature_value not in feature_values:
            feature_values[feature_value] = []
        feature_values[feature_value].append(y[i])
    weighted_entropy = 0.0
    for subset in feature_values.values():
        subset_probability = len(subset) / len(y)
        weighted_entropy += subset_probability * calculate_entropy(subset)
    info_gain = original_entropy - weighted_entropy
    return original_entropy, info_gain, feature_values

# Function to read CSV data
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    X = [row[:-1] for row in data]  # Features are all but the last column
    y = [row[-1] for row in data]   # Target variable is the last column
    return X, y, header

if __name__ == "__main__":
    # Reading the CSV file
    X, y, header = read_csv('datasheet.csv')
    
    # Initial entropy calculation
    initial_entropy = calculate_entropy(y)
    print(f"Initial Entropy of Class: {initial_entropy:.4f}")
    
    # Loop over each feature to calculate information gain
    for feature_index in range(len(X[0])):
        original_entropy, info_gain, feature_values = calculate_information_gain(X, y, feature_index)
        print(f"\nEntropy for feature '{header[feature_index]}': {original_entropy:.4f}")
        for value, subset in feature_values.items():
            sub_entropy = calculate_entropy(subset)
            print(f"  Entropy for '{value}': {sub_entropy:.4f}")
        print(f"Information Gain for feature '{header[feature_index]}': {info_gain:.4f}")
