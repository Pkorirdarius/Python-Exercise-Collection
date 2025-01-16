#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def load_and_preprocess_data():
    # Load the dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y, iris

def split_and_standardize(X, y, test_size=0.3, random_state=42):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test, scaler

def train_and_evaluate_knn(X_train, y_train, X_test, y_test, k_values, distance_metrics):
    results = []
    for k in k_values:
        for metric in distance_metrics:
            knn = KNeighborsClassifier(n_neighbors=k, metric=metric)
            knn.fit(X_train, y_train)
            y_pred = knn.predict(X_test)
            results.append(evaluate_model(y_test, y_pred, k, metric))
    return pd.DataFrame(results, columns=['k', 'Metric', 'Accuracy', 'Precision', 'Recall', 'F1-Score'])

def evaluate_model(y_test, y_pred, k, metric):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    print(f"\nConfusion matrix for k={k}, metric={metric}:")
    print(confusion_matrix(y_test, y_pred))
    print(f"\nClassification report for k={k}, metric={metric}:")
    print(classification_report(y_test, y_pred))
    return (k, metric, accuracy, precision, recall, f1)

def plot_decision_boundaries(X, y, model, feature_names):
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ['red', 'green', 'blue']

    h = 0.01
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=cmap_light)

    for idx, color in enumerate(cmap_bold):
        plt.scatter(X[y == idx, 0], X[y == idx, 1], c=color, label=iris.target_names[idx], edgecolor='k')

    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title("Decision Boundaries (k=3, Euclidean distance)")
    plt.legend()
    plt.show()

def main():
    # Load and preprocess data
    X, y, iris = load_and_preprocess_data()
    X_train, X_test, y_train, y_test, scaler = split_and_standardize(X, y)

    # Train and evaluate kNN
    k_values = [3, 5, 7]


# In[ ]:




