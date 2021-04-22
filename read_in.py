# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:47:46 2020

@author: haile
"""
import json
import pandas as pd
import math
from csv import writer

# calcs the euclidean distance between 2 points
def euclidean_distance(point1, point2):
    sum_sqrd_dist = 0
    for i in range(len(point1)):
        sum_sqrd_dist += math.pow(point1[i]-point2[i], 2)
    return math.sqrt(sum_sqrd_dist)

# finds the ratio between 2 distances
def ratio(dist1, dist2):
    return dist1/dist2

# adds a new row convereted from a list to the database csv
def append_list_as_row(list_el):
    with open('database.csv', 'a+', newline='') as fd:
        write_csv = writer(fd)
        write_csv.writerow(list_el)
        
# adds new patient to the database
def addNewPatient(ratios):
    df = pd.DataFrame(ratios, columns = ['name', 'ratio'])
    df = df.transpose()
    atest = df.iloc[1]
    append_list_as_row(atest)

# sets the current patient
def setCurPatient(ratios): 
    curPatient_df = pd.DataFrame(ratios, columns = ['name', 'ratio'])
    curPatient_df = curPatient_df.transpose()
    ratio_list = curPatient_df.iloc[1]
    
    # overwrite csv wuth new current patient
    with open('curPatient.csv', 'w', newline='') as fd:
        write_csv = writer(fd)
        write_csv.writerow(['ratio 1', 'ratio 2', 'ratio 3', 'ratio 4', 'ratio 5'])
        write_csv.writerow(ratio_list)
        
            
# prompt user for which patient file they would like to get database for
file = input("Enter patient file name:")

# open patient json file 
with open(file + '.JSON', encoding="utf8") as f:
    data = json.load(f)



""" measurements dataframe """
""" 

old code from semester 1

# create empty dataframes for each item needed
df = pd.DataFrame(columns = ['name'])
#desc_df = pd.DataFrame()
#type_df = pd.DataFrame()
value_df = pd.DataFrame()    

# fill each dataframe
for i in range(12): 
    df = df.append({'name': data["measurements"][i]["name"]}, ignore_index = True)  
    #desc_df = desc_df.append({'description' : data["measurements"][i]["description"]}, ignore_index = True)
    #type_df = type_df.append({'type' : data["measurements"][i]["type"]}, ignore_index = True)
    value_df = value_df.append({'value' : data["measurements"][i]["value"]}, ignore_index = True)

# concat each  dataframe to create database of measurements
dfs = [df, value_df]
measurements_df = pd.concat(dfs, axis =1)
"""

""" features dataframe """

# create empty dataframes for each item needed
f_df = pd.DataFrame(columns = ['name'])
#f_desc_df = pd.DataFrame()
#f_type_df = pd.DataFrame()
f_xvals_df = pd.DataFrame()    
f_yvals_df = pd.DataFrame()    
f_zvals_df = pd.DataFrame()    

# fill each dataframe
for j in range(48): 
    f_df = f_df.append({'name': data["features"][j]["abbrv"]}, ignore_index = True)  
    #f_desc_df = f_desc_df.append({'description' : data["features"][j]["description"]}, ignore_index = True)
    #f_type_df = f_type_df.append({'type' : data["features"][j]["type"]}, ignore_index = True)
    f_xvals_df = f_xvals_df.append({'x value' : data["features"][j]["xVal"]}, ignore_index = True)
    f_yvals_df = f_yvals_df.append({'y value' : data["features"][j]["yVal"]}, ignore_index = True)
    f_zvals_df = f_zvals_df.append({'z value' : data["features"][j]["zVal"]}, ignore_index = True)

# concat each  dataframe to create database of measurements
f_dfs = [f_df, f_xvals_df, f_yvals_df, f_zvals_df]
features_df = pd.concat(f_dfs, axis =1)
#final_df = pd.concat([measurements_df, features_df])

f.close()

# export patient data
#final_df.to_csv(file + '_df.csv', index = False)
features_df.to_csv(file + '_df.csv', index = False)


#read_file = pd.read_csv(file + '_df.csv')
#final_df.to_excel(file + '_df.xlsx', index = None, header=True)
features_df.to_excel(file + '_df.xlsx', index = None, header=False)

# read in patient csv
pf_pd = pd.read_csv(file + '_df.csv')
pf_pd = pf_pd.set_index('name')

# pull the needed facial points from the dataframe
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

# prompt user to see if they want to add a new patient or set the current patient
choice = input("Enter 1 to add a new patient to the database \nEnter 2 to set the current patient \n: ")

# if & while statements to handle user choice
while (choice != '1' or choice != '2'):
    if choice == '1':
        addNewPatient(ratios) # calls function
        break
    elif choice == '2':
        setCurPatient(ratios) # calls function
        break
    else:
        print("Invalid Input")
    
        # prompt user to see if they want to add a new patient or set the current patient
        choice = input("Enter 1 to add a new patient to the database \nEnter 2 to set the current patient \n: ")



