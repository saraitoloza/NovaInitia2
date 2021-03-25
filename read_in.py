# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:47:46 2020

@author: haile
"""
import json
import pandas as pd

# prompt user for which patient file they would like to get database for
file = input("Enter patient file name:")

# open patient json file 
with open(file + '.JSON', encoding="utf8") as f:
    data = json.load(f)
 
""" measurements dataframe """
"""
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
