import json
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, kmeans2, whiten

# Read JSON data file
DATA_FILE = 'data.csv'
df = pd.read_csv(DATA_FILE)

# k-means Parameters
# The k-means algorithm groups N observations (i.e. rows in the array of
# coordinates) into k clusters.
coordinates = df.as_matrix()
N = len(coordinates)
k = 500
i = 50
# whiten : Each feature is divided by its standard deviation across all 
# observations to give it unit variance.  i.e., it's supposed to be more
# spatially representative of the original, full data set.
w = whiten(coordinates)

# Cluster
cluster_centroids, closest_centroids = kmeans2(w, k, iter=i)
plt.figure(figsize=(10, 6), dpi=100)
plt.scatter(cluster_centroids[:,0], cluster_centroids[:,1], c='r', s=100)
plt.scatter(w[:,0],w[:,1], c='k', alpha=0.3, s=10)
plt.show()

