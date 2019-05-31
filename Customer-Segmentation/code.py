# --------------
# import packages

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 



# Load Offers
offers=pd.read_excel(path,sheet_name=0)
transactions=pd.read_excel(path,sheet_name=1)
transactions['n']=1
df_list=[offers,transactions]
#df=pd.concat(df_list)
df=pd.merge(offers,transactions,how='inner')
print(df.shape)
print(transactions.shape)
print(df.head())
# Load Transactions



# Merge dataframes


# Look at the first 5 rows



# --------------
# Code starts here

# create pivot table

matrix=df.pivot_table(index='Customer Last Name',columns='Offer #',values='n')
print(matrix)
# replace missing values with 0
matrix.fillna(0,inplace=True)
matrix.reset_index(inplace=True)
print(matrix.head())
# reindex pivot table


# display first 5 rows


# Code ends here


# --------------
# import packages
from sklearn.cluster import KMeans

# Code starts here

# initialize KMeans object
cluster=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
print(matrix.shape)
matrix['cluster']=cluster.fit_predict(matrix[matrix.columns[1:]])
print(matrix.head())
# create 'cluster' column


# Code ends here


# --------------
# import packages
from sklearn.decomposition import PCA

# Code starts here

# initialize pca object with 2 components
pca=PCA(n_components=2,random_state=0)
matrix['x']=cluster.fit_transform(matrix[matrix.columns[1:]])[:,0]

# create 'x' and 'y' columns donoting observation locations in decomposed form
matrix['y']=cluster.fit_transform(matrix[matrix.columns[1:]])[:,1]

# dataframe to visualize clusters by customer names
clusters= matrix.iloc[:,[0,33,34,35]]
print(clusters.head())
clusters.plot.scatter(x = 'x', y = 'y', c = 'cluster', colormap = 'viridis')

# visualize clusters


# Code ends here


# --------------

# merge 'clusters' and 'transactions'
data = pd.merge(clusters, transactions)

# merge `data` and `offers`
data = pd.merge(data, offers)
print(data.head())

# initialzie empty dictionary
champagne = {}

# iterate over every cluster
for i in data['cluster'].unique():
    # observation falls in that cluster
    new_df = data[data['cluster'] == i]
    # sort cluster according to type of 'Varietal'
    counts = data['Varietal'].value_counts(ascending = False)
    print("\n",counts)
    # check if 'Champagne' is ordered mostly
    if (counts.index[0] == 'Champagne'):
        # add it to 'champagne'
        champagne.update({i:counts[0]})

print("cluster dict: ",champagne)
# get cluster with maximum orders of 'Champagne' 
cluster_champagne = max(champagne, key=champagne.get) 

# print out cluster number
print("cluster_champagne: ", cluster_champagne)



# --------------

discount  = {}

# iterate over cluster numbers
for cluster in data['cluster'].unique():
    # dataframe for every cluster
    new_df = data[data['cluster'] == cluster]
    # average discount for cluster
    count = new_df['Discount (%)'].sum()/new_df['Discount (%)'].count()
    # adding cluster number as key and average discount as value 
    discount[cluster] = count

print("discount dict: ", discount)
# cluster with maximum average discount
cluster_discount  = max(discount, key = discount.get)
print("cluster_discount: ", cluster_discount)


