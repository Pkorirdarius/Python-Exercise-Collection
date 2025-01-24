import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Set seed for reproducibility
np.random.seed(42)

# Cluster 1: City Center A (e.g., New York City)
city_center_a = np.random.normal(loc=[40.7128, -74.0060], scale=0.01, size=(500, 2))

# Cluster 2: City Center B (e.g., Los Angeles)
city_center_b = np.random.normal(loc=[34.0522, -118.2437], scale=0.01, size=(500, 2))

# Outliers: Random locations across the country
outliers = np.random.uniform(low=[25, -125], high=[50, -65], size=(50, 2))

# Combine all points
coordinates = np.vstack((city_center_a, city_center_b, outliers))
df = pd.DataFrame(coordinates, columns=["Latitude", "Longitude"])

# Standardize features
scaler = StandardScaler()
scaled_coordinates = scaler.fit_transform(df[["Latitude", "Longitude"]])

# Apply DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=10)
dbscan.fit(scaled_coordinates)

# Assign cluster labels
df["Cluster"] = dbscan.labels_

# Map cluster labels to colors
cluster_labels = df["Cluster"].unique()
colors = plt.cm.get_cmap("tab20", len(cluster_labels))

plt.figure(figsize=(12, 8))
for cluster, color in zip(cluster_labels, colors.colors):
    subset = df[df["Cluster"] == cluster]
    plt.scatter(
        subset["Longitude"],
        subset["Latitude"],
        color=color,
        label=f"Cluster {cluster}" if cluster != -1 else "Outliers",
        s=50,
    )

plt.title("DBSCAN Clustering of Delivery Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.show()
