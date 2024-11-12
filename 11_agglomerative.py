import csv

def read_distance_matrix(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        labels = next(reader)
        distance_matrix = []
        for row in reader:
            distance_matrix.append([float(value) if value else 0 for value in row[1:]])
    return labels[1:], distance_matrix

def single_linkage(matrix, cluster1, cluster2):
    return min(matrix[cluster1][cluster2], matrix[cluster2][cluster1])

def complete_linkage(matrix, cluster1, cluster2):
    return max(matrix[cluster1][cluster2], matrix[cluster2][cluster1])

def average_linkage(matrix, cluster1, cluster2, clusters):
    size1 = len(clusters[cluster1])
    size2 = len(clusters[cluster2])
    return (size1 * matrix[cluster1][cluster2] + size2 * matrix[cluster2][cluster1]) / (size1 + size2)

def cluster_distance_from_matrix(matrix, i, j, linkage_type, clusters):
    if linkage_type == "single":
        return single_linkage(matrix, i, j)
    elif linkage_type == "complete":
        return complete_linkage(matrix, i, j)
    elif linkage_type == "average":
        return average_linkage(matrix, i, j, clusters)

def print_distance_table(clusters, matrix):
    n = len(clusters)
    cluster_names = ["[" + ', '.join(cluster) + "]" for cluster in clusters]
    max_len = max(len(name) for name in cluster_names)
    
    print("\nDistance Matrix:")
    header = " " * (max_len + 2) + "  ".join(f"{name:>{max_len}}" for name in cluster_names)
    print(header)
    
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append("0.00")
            else:
                row.append(f"{matrix[i][j]:.2f}")
        row_str = f"{cluster_names[i]:>{max_len}} " + "  ".join(f"{value:>{max_len}}" for value in row)
        print(row_str)

def agglomerative_clustering(matrix, labels, linkage_type):
    clusters = [[label] for label in labels]
    
    while len(clusters) > 1:
        print_distance_table(clusters, matrix)
        min_distance = float('inf')
        clusters_to_merge = None

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = cluster_distance_from_matrix(matrix, i, j, linkage_type, clusters)
                if dist < min_distance:
                    min_distance = dist
                    clusters_to_merge = (i, j)

        if clusters_to_merge:
            cluster1, cluster2 = clusters_to_merge
            print(f"Merging clusters: {clusters[cluster1]} and {clusters[cluster2]}")
            clusters[cluster1] += clusters[cluster2]
            del clusters[cluster2]

            
            for k in range(len(matrix)):
                if k != cluster1 and k != cluster2:
                    matrix[cluster1][k] = min(matrix[cluster1][k], matrix[cluster2][k]) if linkage_type == "single" else max(matrix[cluster1][k], matrix[cluster2][k])
                    matrix[k][cluster1] = matrix[cluster1][k]

            matrix = [row[:cluster2] + row[cluster2+1:] for row in matrix]
            matrix.pop(cluster2)

    return clusters

def main():
    labels, matrix = read_distance_matrix('matrix.csv')
    
    
    print("\nChoose a linkage method for agglomerative clustering:")
    print("1. Single Linkage")
    print("2. Complete Linkage")
    print("3. Average Linkage")
        
    choice = input("Enter your choice (1-3): ")
        
    if choice == '1':
        linkage_type = "single"
    elif choice == '2':
        linkage_type = "complete"
    elif choice == '3':
        linkage_type = "average"
    
        
    print(f"\nFinal Clusters: {agglomerative_clustering(matrix, labels, linkage_type)}")

if __name__ == '__main__':
    main()
