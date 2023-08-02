import pandas as pd
import numpy as np

# define distance calculation function
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y)**2))

# define centroid calculation function
def calculate_centroid(X, cluster_labels, cluster):
    return np.mean(X[cluster_labels == cluster], axis=0)

# define function to calculate sum squared error
def calculate_sse(X, cluster_labels, centroids):
    sse = 0
    for i in range(len(X)):
        sse += euclidean_distance(X[i], centroids[cluster_labels[i]])
    return sse

# read data from CSV file
data = pd.read_csv('data_sample.csv')

# select the features to use for clustering
X = data[['feature1', 'feature2', 'feature3']].values

# set number of clusters
k = int(input("Enter the number of clusters (k): "))

# set convergence criteria
max_iter = 40
threshold = 1e-5

# initialize centroids
centroids = X[np.random.choice(len(X), k)]

# iterate until convergence
for i in range(max_iter):
    # assign points to clusters
    cluster_labels = np.argmin(np.array([euclidean_distance(x, centroids) for x in X]), axis=1)
    
    # calculate new centroids
    new_centroids = np.zeros((k, X.shape[1]))
    for j in range(k):
        new_centroids[j,:] = calculate_centroid(X, cluster_labels, j)
    
    # check for convergence
    if np.allclose(centroids, new_centroids, rtol=threshold):
        break
    
    # update centroids
    centroids = new_centroids

# print sum squared error value
sse = calculate_sse(X, cluster_labels, centroids)
print(f'Sum squared error for k={k}: {sse}')
