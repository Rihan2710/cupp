import csv
import math

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

def calculate_gini_index(y):
    label_counts = {}
    for label in y:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    total_count = len(y)
    gini = 1.0
    for count in label_counts.values():
        probability = count / total_count
        gini -= probability ** 2
    return gini

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

def calculate_gini_for_feature(X, y, feature_index):
    feature_values = {}
    for i in range(len(X)):
        feature_value = X[i][feature_index]
        if feature_value not in feature_values:
            feature_values[feature_value] = []
        feature_values[feature_value].append(y[i])
    weighted_gini = 0.0
    for subset in feature_values.values():
        subset_probability = len(subset) / len(y)
        weighted_gini += subset_probability * calculate_gini_index(subset)
    return weighted_gini, feature_values

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    X = [row[:-1] for row in data]
    y = [row[-1] for row in data]
    return X, y, header

if __name__ == "__main__": 
    X, y, header = read_csv('table2.csv')
    initial_entropy = calculate_entropy(y)
    initial_gini = calculate_gini_index(y)
    print(f"Initial Entropy: {initial_entropy:.4f}")
    print(f"Initial Gini Index: {initial_gini:.4f}")
    for feature_index in range(len(X[0])):
        original_entropy, info_gain, feature_values = calculate_information_gain(X, y, feature_index)
        weighted_gini, feature_values = calculate_gini_for_feature(X, y, feature_index)
        print(f"\nEntropy for feature '{header[feature_index]}': {original_entropy:.4f}\n")
        print(f"{'Value':<15}{'Entropy':<15}{'Gini Index':<15}")
        print("-" * 50)
        for value, subset in feature_values.items():
            sub_entropy = calculate_entropy(subset)
            sub_gini = calculate_gini_index(subset)
            print(f"{value:<15}{sub_entropy:<15.4f}{sub_gini:<15.4f}")
        print(f"\nInformation Gain for feature '{header[feature_index]}': {info_gain:.4f}")
        print(f"Gini Index for feature '{header[feature_index]}': {weighted_gini:.4f}")
        print("=" * 50)
