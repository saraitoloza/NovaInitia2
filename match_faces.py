# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:18:20 2021

@author: hailey
"""
import math
from collections import Counter
import pandas as pd

def euclidean_distance(point1, point2):
    sum_sqrd_dist = 0
    for i in range(len(point1)):
        sum_sqrd_dist += math.pow(point1[i]-point2[i], 2)
    return math.sqrt(sum_sqrd_dist)

def ratio(dist1, dist2):
    return dist1/dist2

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

# prompt user for which patient file they would like to get database for
file = input("Enter patient file name:")

# read in patient csv
pf_pd = pd.read_csv(file + '_df.csv')
#pf_pd = pd.read_csv('Pt1_df.csv')
pf_pd = pf_pd.set_index('name')

# pull the points from the dataframe
ex_r = [pf_pd.loc['ex_r']['x value'], pf_pd.loc['ex_r']['y value'],pf_pd.loc['ex_r']['z value']]
ex_l = [pf_pd.loc['ex_l']['x value'], pf_pd.loc['ex_l']['y value'],pf_pd.loc['ex_l']['z value']]

ch_r = [pf_pd.loc['ch_r']['x value'], pf_pd.loc['ch_r']['y value'],pf_pd.loc['ch_r']['z value']]
ch_l = [pf_pd.loc['ch_l']['x value'], pf_pd.loc['ch_l']['y value'],pf_pd.loc['ch_l']['z value']]

en_r = [pf_pd.loc['en_r']['x value'], pf_pd.loc['en_r']['y value'],pf_pd.loc['en_r']['z value']]
en_l = [pf_pd.loc['en_l']['x value'], pf_pd.loc['en_l']['y value'],pf_pd.loc['en_l']['z value']]

tr = [pf_pd.loc['tr']['x value'], pf_pd.loc['tr']['y value'],pf_pd.loc['tr']['z value']]
g = [pf_pd.loc['g']['x value'], pf_pd.loc['g']['y value'],pf_pd.loc['g']['z value']]

sto = [pf_pd.loc['sto']['x value'], pf_pd.loc['sto']['y value'],pf_pd.loc['sto']['z value']]
me = [pf_pd.loc['me']['x value'], pf_pd.loc['me']['y value'],pf_pd.loc['me']['z value']]

n = [pf_pd.loc['n']['x value'], pf_pd.loc['n']['y value'],pf_pd.loc['n']['z value']]
sn = [pf_pd.loc['sn']['x value'], pf_pd.loc['sn']['y value'],pf_pd.loc['sn']['z value']]

zy_r = [pf_pd.loc['zy_r']['x value'], pf_pd.loc['zy_r']['y value'],pf_pd.loc['zy_r']['z value']]
zy_l = [pf_pd.loc['zy_l']['x value'], pf_pd.loc['zy_l']['y value'],pf_pd.loc['zy_l']['z value']]

# calculate the ratios of the euclidean distances and add to new dataframe
ratios = [ ['intercanthal/interchillion', ratio(euclidean_distance(ex_r, ex_l), euclidean_distance(ch_r, ch_l))],
          ['interchilion/interdacryon' , ratio(euclidean_distance(ch_r, ch_l), euclidean_distance(en_r, en_l))],
          ['forehead height/stomion-soft menton', ratio(euclidean_distance(tr, g), euclidean_distance(sto, me))],
          ['soft menton-nasion/subnasale-stomion', ratio(euclidean_distance(g, n), euclidean_distance(sn, sto))],
          ['trichion-menton/zygions', ratio(euclidean_distance(tr, me), euclidean_distance(zy_r, zy_l))]
          ]

df = pd.DataFrame(ratios, columns = ['name', 'ratio'])




"""
# testing
point1 = [2,4,3]
point2 = [3,8,2]

print("{:.2f}".format(euclidean_distance(point1, point2)))
"""