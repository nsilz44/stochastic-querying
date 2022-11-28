import random
import numpy as np


def minimumProblem(num_of_intervals,salt_max,query_cost_uniformness,query_cost_max,probability_distribution_list):
    Li = []
    current_point = 0
    for i in range (0,num_of_intervals):
        salt = random.uniform(0,salt_max)
        current_point += salt
        Li.append(current_point)
    Ri =[]
    for i in range (0,num_of_intervals):
        salt = random.uniform(0,salt_max)
        current_point += salt
        Ri.append(current_point)
    
    if query_cost_uniformness == 1:
        Qi = [query_cost_max] * num_of_intervals
    return Li,Ri,Qi,probability_distribution_list

def hypergraphOrientationProblem(num_of_intervals,num_of_edges,max_vertices_per_edge,salt_max,query_cost_uniformness,query_cost_max,probability_distribution_list):
    Li = []
    current_point = 0
    for i in range (0,num_of_intervals):
        salt = random.uniform(0,salt_max)
        current_point += salt
        Li.append(current_point)
    Ri =[]
    for i in range (0,num_of_intervals):
        salt = random.uniform(0,salt_max)
        current_point += salt
        Ri.append(current_point)
    if query_cost_uniformness == 1:
        Qi = [query_cost_max] * num_of_intervals
    Ei = []
    for i in range (0,num_of_edges):
        verticesInEdge = random.randint(1,max_vertices_per_edge)
        edge = list(np.random.permutation(np.arange(0,num_of_intervals))[:verticesInEdge])
        Ei.append(edge)
    
    if query_cost_uniformness == 1:
        Qi = [query_cost_max] * num_of_intervals
    return Li,Ri,Ei,Qi,probability_distribution_list

#p= 10 * [1]
#print(minimumProblem(10,10,1,1,p))
#print(hypergraphOrientationProblem(10,8,3,10,1,1,p))
