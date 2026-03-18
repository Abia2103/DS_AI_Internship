from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 1. Generate data
X = np.random.randn(50, 2) + [2, 2]
X2 = np.random.randn(50, 2) + [-2, -2]
X_final = np.vstack([X, X2])

inertia = []
K_range = range(1, 11)

for k in K_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_final)
    inertia.append(model.inertia_)

print("K values tested: ", list(K_range))
print("Inertia values: ", [round(i, 2) for i in inertia])


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Fit K-Means
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_final)

# 3. Get Centroids
centers = kmeans.cluster_centers_

print(f"Total points: {len(X_final)}")
print(f"Centroid 1: {centers[0]}")
print(f"Centroid 2: {centers[1]}")
plt.scatter(X_final[:,0], X_final[:,1], c=labels)
plt.show()

