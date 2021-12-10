import pandas
from sklearn.cluster import KMeans
import matplotlib.pyplot as pyplot

from sklearn.metrics import silhouette_score

data = pandas.read_csv("dataset_final.csv")
data = data.values

print(data)