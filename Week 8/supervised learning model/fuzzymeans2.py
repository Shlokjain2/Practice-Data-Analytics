import pandas as pd
import numpy as np

# read data from CSV file
data = pd.read_csv('data_sample.csv')

# select the features to use for clustering
X = data[['feature1', 'feature2', 'feature3']].values

# set number of clusters
k = 3

# set fuzziness exponent
m = 1.26

# set c parameter
c = 2

# initialize membership matrix
membership = np.random.rand(len(X), k)

# normalize membership matrix
membership = membership / np.sum(membership, axis=1, keepdims=True)

# set maximum number of iterations
max_iter = 100

# iterate until convergence
for i in range(max_iter):
    # calculate centroids
    centroids = np.zeros((k, X.shape[1]))
    for j in range(k):
        centroids[j,:] = np.sum(membership[:,j]**m * X.T, axis=1) / np.sum(membership[:,j]**m)
    
    # calculate distance matrix
    distance = np.zeros((len(X), k))
    for j in range(k):
        distance[:,j] = np.sqrt(np.sum((X - centroids[j,:])**2, axis=1))
    
    # calculate new membership matrix
    new_membership = np.zeros((len(X), k))
    for j in range(k):
        new_membership[:,j] = 1 / np.sum((distance[:,j] / distance)**(2/(m-1)), axis=1)
    new_membership = new_membership / np.sum(new_membership, axis=1, keepdims=True)
    
    # check for convergence
    if np.allclose(new_membership, membership):
        break
    
    # update membership matrix
    membership = new_membership

# get the final clustering
cluster_labels = np.argmax(membership, axis=1)
