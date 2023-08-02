import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the water sample data set into a Pandas dataframe
water_samples = pd.read_csv('path/to/water_samples.csv')

# Select two features for clustering
X = water_samples[['feature1', 'feature2']].values

# Apply k-means clustering with k=2
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Plot the clusters
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200, alpha=0.5)
plt.show()

# Find the optimal value of k using the elbow method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia)
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
