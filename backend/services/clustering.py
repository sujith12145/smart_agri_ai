from sklearn.cluster import DBSCAN
import numpy as np

def cluster_cases(locations):
    db = DBSCAN(eps=0.5, min_samples=3).fit(locations)
    return db.labels_