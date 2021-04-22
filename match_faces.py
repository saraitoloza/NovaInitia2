# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:18:20 2021

@author: hailey
"""
import math
import pandas as pd
from csv import writer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns


def euclidean_distance(point1, point2):
    sum_sqrd_dist = 0
    for i in range(len(point1)):
        sum_sqrd_dist += math.pow(point1[i]-point2[i], 2)
    return math.sqrt(sum_sqrd_dist)

def getNeighbors(patient, df):
       
    # calc euclidean distance between patient and database points
    dist_list = []
    dfPatient = []
    for i in range (len(df['ratio 2'])):
        dist = euclidean_distance([patient.loc[0]['ratio 2'], patient.loc[0]['ratio 5']], [df.loc[i]['ratio 2'], df.loc[i]['ratio 5']])
        dfPatient.append(df.loc[i]['patient'])
        dist_list.append(dist) 
    
    data = pd.DataFrame({'patient': dfPatient, 'distance': dist_list})
    data = data.sort_values('distance')
        
    return data.head(3)

df = pd.read_csv('database.csv')

# normalize data set
"""

norm_r1 = pd.DataFrame((preprocessing.normalize([np.array(df['ratio 1'])])).transpose())
norm_r2 = pd.DataFrame((preprocessing.normalize([np.array(df['ratio 2'])])).transpose())
norm_r3 = pd.DataFrame((preprocessing.normalize([np.array(df['ratio 3'])])).transpose())
norm_r4 = pd.DataFrame((preprocessing.normalize([np.array(df['ratio 4'])])).transpose())
norm_r5 = pd.DataFrame((preprocessing.normalize([np.array(df['ratio 5'])])).transpose())

norm_df = pd.concat([norm_r1, norm_r2, norm_r3, norm_r4, norm_r5], axis = 1)

norm_df.to_csv('norm_database.csv', index = False)


norm_df = pd.read_csv('norm_database.csv')
"""

df.head()
df['class'].unique()
df.isnull().values.any()

df['class'] = df['class'].map({'faces-1' :0, 'faces-2' :1, 'faces-3' :2}).astype(int) #mapping numbers
df.head()

plt.close()
sns.set_style('whitegrid');
sns.pairplot(df, hue = 'class', height = 3);
plt.show()

sns.set_style('whitegrid');
sns.FacetGrid(df, hue='class', size=5) \
.map(plt.scatter, 'ratio 2', 'ratio 5') \
.add_legend();
plt.show()

x_data = df.drop(['class', 'patient', 'ratio 4', 'ratio 3', 'ratio 1'], axis=1)

y_data = df['class']

# normalize data
MinMaxScaler = preprocessing.MinMaxScaler()
X_data_minmax = MinMaxScaler.fit_transform(x_data)

data = pd.DataFrame(x_data, columns = ['ratio 2', 'ratio 5'])
df.head()

X_train, X_test, y_train, y_test = train_test_split(data, y_data, test_size=0.2, random_state = 1)

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train,y_train)
ypred = knn_clf.predict(X_test) #These are the predicted output values

result = confusion_matrix(y_test, ypred)
print('Confusion Matrix:')
print(result)
result1 = classification_report(y_test, ypred)
print('Classification Report:',)
print (result1)
result2 = accuracy_score(y_test,ypred)
print('Accuracy:',result2)

#some kind of action that connects with button
curPatient = pd.read_csv('curPatient.csv')

kNeighbors = getNeighbors(curPatient, df)