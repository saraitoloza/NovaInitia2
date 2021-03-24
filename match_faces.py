# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:18:20 2021

@author: hailey
"""
import math
from collections import Counter

def euclidean_distance(point1, point2):
    sum_sqrd_dist = 0
    for i in range(len(point1)):
        sum_sqrd_dist += math.pow(point1[i]-point2[i], 2)
    return math.sqrt(sum_sqrd_dist)

def mean(labels):
    return sum(labels)/len(labels)

def mode(labels):
    return Counter(labels).most_common(1)[0][0]

# k-NN algorithm to find matching faces
def knn(data, query, k, distance_fn, choice_fn):
    neighbor_dist_ind = []
    
    # doing for each example in the data
    for index, example in enumerate(data):
        
        # calc the distance between the query example and cur example
        distance = distance_fn(example[:-1], query)
        
        # add the distance and the index of the example to an ordered collection
        neighbor_dist_ind.append((distance, index))
        
    # sort the ordered collection from smallest to largest
    sorted_neighbor_dist_ind = sorted(neighbor_dist_ind)
    
    # pick the first k entries from sorted
    k_nearest = sorted_neighbor_dist_ind[:k]
    
    # get the labels for the k entries
    k_nearest_labels = [data[i][-1] for distance, i in k_nearest]
    
    return k_nearest, choice_fn(k_nearest_labels)

# initialize k
k = 3


# testing
point1 = [2,4,3]
point2 = [3,8,2]

print("{:.2f}".format(euclidean_distance(point1, point2)))