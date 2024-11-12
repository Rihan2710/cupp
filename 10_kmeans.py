import csv
import random

def read_data_from_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            data.append([float(row[0]), float(row[1])])
    return data

def calculate_centroid(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    centroid = [sum(x_coords) / len(points), sum(y_coords) / len(points)]
    return centroid

def calculate_distance(point1, point2):
    return (sum((x - y) ** 2 for x, y in zip(point1, point2)))**0.5

def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = [calculate_distance(point, centroid) for centroid in centroids]
        min_distance_index = distances.index(min(distances))
        clusters[min_distance_index].append(point)
    return clusters

def update_centroids(clusters):
    return [calculate_centroid(cluster) for cluster in clusters]

def kmeans(data, k, max_iterations=100):
    centroids = random.sample(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters, centroids

def display_clusters(clusters):
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i+1}:")
        for point in cluster:
            print(f"    {point}")

def print_centroids(centroids):
    print("Centroids:")
    for i, centroid in enumerate(centroids):
        print(f"    Centroid {i+1}: {centroid}")

def print_distance_matrix(data, centroids):
    print("Distance Matrices:")
    for i, centroid in enumerate(centroids):
        print(f"Distance matrix for Centroid {i+1}:")
        distances = [calculate_distance(point, centroid) for point in data]
        for j in range(len(distances)):
            for k in range(j + 1):
                print(f"{distances[k]:.2f}", end=" ")
            print()

def main():
    filename = 'circles.csv'
    data = read_data_from_csv(filename)
    
    k = int(input("Enter the number of clusters: "))
    
    clusters, centroids = kmeans(data, k)
    
    display_clusters(clusters)
    print_centroids(centroids)
    print_distance_matrix(data, centroids)

if __name__ == '__main__':
    main()
