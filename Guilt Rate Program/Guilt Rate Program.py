from warnings import filterwarnings
filterwarnings('ignore')
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from sklearn.cluster import KMeans


usa=pd.read_csv("USArrests.csv")
df=usa.copy()

df.index=df["Unnamed: 0"]

df=df.drop("Unnamed: 0",axis=1)

df.index.name="Eyalet"


df.head()

from yellowbrick.cluster import KElbowVisualizer

k_means=KMeans()
k_cv=KElbowVisualizer(k_means,k=(2,10))
visualize=k_cv.fit(df)
visualize.poof();


k_means_final=KMeans(n_clusters=4)
k_means_final_model=k_means_final.fit(df)

labels=k_means_final_model.labels_

merkezler=k_means_final_model.cluster_centers_

merkezler


labels=list(labels)
uzunluk=len(labels)

for i in range(uzunluk):
    
    if labels[i]==1:
        labels[i]=4
    
    if labels[i]==2:
        labels[i]=3
        
    if labels[i]==3:
        labels[i]=2
        
    if labels[i]==0:
        labels[i]=1


