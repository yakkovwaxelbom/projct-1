import random
import tqdm
import numpy as np
from collections import defaultdict


# def cluster_means(k: int,
#                   inputs: list[np.array],
#                   assignments: list[int]) -> list[np.array]:
#     # clusters[i] contains the inputs whose assignment is i
#     clusters = [[] for i in range(k)]
#     for input, assignment in zip(inputs, assignments):
#         clusters[assignment].append(input)
#         # if a cluster is empty, just use a random point
#         return [vector_mean(cluster) if cluster else random.choice(inputs)
#                 for cluster in clusters]


class KMeans:
    def __init__(self, samples, k: int, d=3) -> None:
        self.samples = samples
        self.k = k
        self.d = d
        # number of clusters
        self.means = np.random.randint(0, 255, (k, d))
        self.clusters = None

    def __classify(self):
        self.clusters = np.array([np.argmin(np.sum((sample - self.means) ** 2, axis=1))
                                  for sample in self.samples])

    def __mean(self, ):
        new_means = []
        location_each_cluster = [[] for _ in range(self.k)]
        for i, cluster in enumerate(self.clusters):
            location_each_cluster[cluster].append(i)

        for item in location_each_cluster:
            new_means.append(np.array(np.mean(self.samples[item], axis=0) if item else random.choice(self.samples)))
        return np.array(new_means)

    def train(self):
        self.__classify()
        nwe_mean = self.__mean()
        while not np.array_equal(nwe_mean, self.means):
            self.means = nwe_mean
            self.__classify()
            nwe_mean = self.__mean()
        return self.means, self.clusters


# a = np.array([[0, 4], [2, 0], [4, 3], [8, 0]])
# a = np.random.randint(0, 10, (4, 2))
# b = np.array([[1, 1], [2, 3, ]])
# print(a)
# print(b)
# print( np.zeros((4, 3)))
# print(np.array([np.argmin(np.sum((a - b[0]) ** 2, axis=1))]))
#
# matrix = np.array([[1, 2, 4, 4], [5, 6, 7, 8], [9, 10, 11, 12], [2, 5, 6, 8]])
#
# rows = [[0, 2], []]
# new_means = []
# for row in rows:
    # new_means.append(np.mean(matrix[row], axis=1) if row else random.choice(matrix))
# new_means = np.array(new_means)
# means = np.mean(matrix[rows[0]], axis=1)
# print(new_means)
# print(means)
# a = [1, 1, 1, 2, 3, 34, 5, 6, 7, ]
# print([(a, b) for a, b in enumerate(a)])
a =np.array([[1, 2, 3], [2, 6, 4]])

b =np.array([[1, 2, 3], [2, 3, 4]])
#
while not np.array_equal(a, b):
    print('ok')
