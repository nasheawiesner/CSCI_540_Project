from CSCI_540_Project import PreProcess
from CSCI_540_Project import K_Means
import math


def main():
    input = PreProcess.parse()
    clusters = []
    k = 25
    clusters_temp = K_Means.K_Means(input, k).get_clusters()
    for cluster in clusters_temp:
        clusters.append(cluster.points)
    evaluate_cluster(clusters)

def get_distance( a, b):  # euclidean distance between two n-dimensional points
    difference = 0.0
    for i in range(len(a)):
        squareDifference = pow(((a[i]) - b[i]), 2)
        difference += squareDifference
    distance = math.sqrt(difference)
    return distance

def evaluate_cluster(clusters):    #handler for calculating the cohesion and separation of the formed clusters
    coh = 0
    sep = 0
    for cluster1 in clusters:
        coh += cohesian(cluster1)
        for cluster2index in range(clusters.index(cluster1), len(clusters)):
            if cluster1 != clusters[cluster2index]:
                sep += separation(cluster1, clusters[cluster2index])
    print("\nCohesion:", coh)
    print("\nSeperation: ", sep)

def cohesian(cluster):
    """Computes the cohesian of the cluster set
    by comparing the intra distance of the cluster
    for all points and dividing by the number of
    instances in the cluster.  The smaller the
    cohesian, the better."""
    cohesian = 0
    for x in cluster:
        for y in cluster:
            if x != y:
                cohesian += get_distance(x,y)
        if len(cluster) != 0:
            cohesian = cohesian / len(cluster)
        else:
             pass
    return cohesian

def separation(c1, c2):
    """Calculates the separation of the cluster set
    by calculating the difference for every point in
    cluster 1 to every element in cluster two.  These
    difference are summed together.  The higher the
    separation, the better."""
    sep = 0
    for x in c1:
        for y in c2:
            sep += get_distance(x,y)
    return sep



if __name__ == '__main__':
    main()