import csv

def load_dataset(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        dataset = list(reader)
    return dataset[1:]

def separate_features_labels(dataset):
    features = []
    labels = []
    for row in dataset:
        # Convert features to appropriate types
        outlook = {'sunny': 0, 'overcast': 1, 'rain': 2}[row[0]]  # Categorical encoding
        temperature = float(row[1])  # Convert to float
        humidity = float(row[2])      # Convert to float
        windy = 0 if row[3] == 'FALSE' else 1  # Convert to binary
        features.append([outlook, temperature, humidity, windy]) 
        labels.append(row[4])  
    return features, labels

def calculate_prior(labels):
    total_count = len(labels)
    label_count = {}
    for label in labels:
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    prior = {label: count / total_count for label, count in label_count.items()}
    return prior

def calculate_conditional_probabilities(features, labels):
    conditional_probabilities = {}
    label_count = {}
    
    for i in range(len(features)):
        label = labels[i]
        if label not in conditional_probabilities:
            conditional_probabilities[label] = {}
            label_count[label] = 0
        label_count[label] += 1
        
        for j in range(len(features[i])):
            if j not in conditional_probabilities[label]:
                conditional_probabilities[label][j] = []
            conditional_probabilities[label][j].append(features[i][j])
    
    for label in conditional_probabilities:
        for j in conditional_probabilities[label]:
            mean = sum(conditional_probabilities[label][j]) / label_count[label]
            variance = sum((x - mean) ** 2 for x in conditional_probabilities[label][j]) / label_count[label]
            conditional_probabilities[label][j] = (mean, variance)
    
    return conditional_probabilities

def calculate_class_probability(sample, prior, conditional_probabilities):
    total_prob = {}
    
    for label in prior:
        prob = prior[label]
        for j in range(len(sample)):
            mean, variance = conditional_probabilities[label][j]
            prob *= (1 / ((2 * 3.14159 * variance) ** 0.5)) * \
                     (2.71828 ** (-((sample[j] - mean) ** 2) / (2 * variance)))
        total_prob[label] = prob
    
    return total_prob

def predict(sample, prior, conditional_probabilities):
    probabilities = calculate_class_probability(sample, prior, conditional_probabilities)
    return max(probabilities, key=probabilities.get)

def main():
    filename = 'table2.csv'  
    dataset = load_dataset(filename)
    features, labels = separate_features_labels(dataset)
    
    prior = calculate_prior(labels)
    conditional_probabilities = calculate_conditional_probabilities(features, labels)

    random_sample = [float(x) for x in input("Enter sample features separated by commas (OUTLOOK, TEMPERATURE, HUMIDITY, WINDY): ").split(',')]
    predicted_class = predict(random_sample, prior, conditional_probabilities)

    print("Sample features:", random_sample)
    print("Predicted class:", predicted_class)
    probabilities = calculate_class_probability(random_sample, prior, conditional_probabilities)
    print("Class probabilities:")
    for label, probability in probabilities.items():
        print(f"Class {label}: {probability:.4f}")

if __name__ == "__main__":
    main()
