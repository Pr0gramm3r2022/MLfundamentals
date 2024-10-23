# -*- coding: utf-8 -*-
"""Machine Learning Assignment 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QzFKkBoq_ZQ3s6N3_D2_An-joAtqzrv_
"""

import os
import tensorflow as tf
import PIL as Image
import matplotlib.pyplot as plt
import sklearn as sk
import pandas as pd
from numpy import random




IrisDf = pd.read_csv("iris.csv")
kmtestDf = pd.read_csv("kmtest (1).csv")

IrisArray = np.asarray(IrisDf)
kmtestArray = np.asarray(kmtestDf)

#collecting information about the arrays I'm doing the algorithms on
print(IrisArray.ndim)
print(IrisArray.shape)
print(IrisDf.head)


#making a plot of attributes of the array

#IrisHistogram = IrisDf[['setosa','virginica']] #giving traceback errors. need to debug and adjust

#plotting the images

#step 1: turn the numpy arrays into an image

#make the images into tensors and transform to images

#IrisTensor = torch.tensor(int32(IrisDf.values)) #giving me issues converting to a tensor

print(IrisArray.dtype)
print(IrisArray.shape)

#Euclidean distance function
def euclidean_distance(x1, x2, x3):
    return np.sqrt(np.sum((x1 + x2 + x3)**2)) #had a minus sign before

    print(euclidean_distance(x1, x2, x3))




#create a for loop to randomly grab points in the matrix and pass them through the Euclidean function

def z_score(og, mean, std_dev):
  return (og - mean) / std_dev

'''x = random.choice(IrisArray[0:9])
y = random.choice(IrisArray[:1])
z = random.choice(IrisArray[:2])

print(x)'''

features = ["sepal_length", "sepal_width", "pedal_length", "pedal_width", "species"] #to cluster Iris data

class KmeansClustering:
  def init (self, k = 3):
    selfk = k
    self.centroids = None

    @staticmethod
    def euclidean_distance(data_point, centroids):
      return np.sqrt(np.sum((centroids - data_point)**2, axis=1))

    def fit(self, X, max_iterations=200):
    # Initialize centroids randomly within the min/max range of X
     self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0),
                                        size=(self.k, X.shape[1]))

    for _ in range(max_iterations):
        y = []


        for data_point in X:

            distances = KmeansClustering.euclidean_distance(data_point, self.centroids)
            cluster_num = np.argmin(distances)
            y.append(cluster_num)

        y = np.array(y)

        cluster_indices = []

        for i in range(self.k):
          cluster_indices.append(np.argwhere(y == i))

        cluster_centers = []


        for i, indices in enumerate(cluster_indices):
          if len(indices) == 0:
            cluster_centers.append(self.centroids[i])
          else:
            cluster_centers.append(np.mean(X[indices],axis = 0)[0])
          if np.max(sewlf.centroids - np.array(cluster_centers)) < 0.001:
            break
          else:
            self.centroids = np.array(cluster_centers)

        return y






        for i in range(self.k):
            points_assigned_to_centroid = X[np.array(y) == i]
            if len(points_assigned_to_centroid) > 0:
                self.centroids[i] = np.mean(points_assigned_to_centroid, axis=0)

  random_points = np.random.randint(0, 100, size=(100, 2))

kmeans = KMeansClustering(k=3)
labels = kmeans.fit(random_points)

#random_points = np.random.randint((0, 100, (100, 2)))
random_points = np.random.randint(0, 100, size=(100, 2))

kmeans = KMeansClustering(k=3)
labels = kmeans.fit(random_points)

plt.scatter(random_points[:,0], random_points[:, 1], c=labels)
plt.scatter(kmeans.centroids[:,0], kmeans.centroids[:, 1], c=range(len(kmeans.centroids)),
            marker='*', s = 200)

plt.show()

