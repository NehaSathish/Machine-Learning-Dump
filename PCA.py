from sklearn.datasets import load_iris
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

iris = load_iris()

data = iris["data"]
target = iris["target"]
mean_centric_data = np.copy(data)
mean = []
features = int(data.size/len(data))
for i in range(features):
    mean.append(data[:,i].mean())
for i in range(len(data)):
    for j in range(features):
        mean_centric_data[i,j] -= mean[j]

sigma = np.cov(mean_centric_data.transpose())

eigen = (la.eig(sigma))
eigen_val = np.copy(eigen[0])
eigen_vec = np.copy(eigen[1].transpose())
eigen_val = list(zip(eigen_val,eigen_vec))
eigen_val.sort()
eigen_val.reverse()

lst = []
for i in range(2):
    lst.append(eigen_val[i][1])
lst = np.asarray(lst)

reduced_data = np.matmul(lst,data.transpose())

plt.scatter(reduced_data[0],reduced_data[1])