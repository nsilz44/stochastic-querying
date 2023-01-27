import random
import numpy as np

# function to exclude lower number from random.uniform to hold assumptions
def randomUniform(low,high):
    i = 0
    while i == 0:
        i = random.uniform(low,high)
    return i

def minimumProblem(num_of_intervals,salt_max,Qi,Pi):
    Li = []
    current_point = 0
    for i in range (0,num_of_intervals):
        salt = randomUniform(0,salt_max)
        current_point += salt
        Li.append(current_point)
    Ri =[]
    for i in range (0,num_of_intervals):
        salt = randomUniform(0,salt_max)
        current_point += salt
        Ri.append(current_point)
    
    return Li,Ri,Qi,Pi

def hypergraphOrientationProblem(num_of_intervals,num_of_edges,max_vertices_per_edge,salt_max,Qi,probability_distribution_list):
    Li = []
    current_point = 0
    for i in range (0,num_of_intervals):
        salt = randomUniform(0,salt_max)
        current_point += salt
        Li.append(current_point)
    Ri =[]
    for i in range (0,num_of_intervals):
        salt = randomUniform(0,salt_max)
        current_point += salt
        Ri.append(current_point)
    Ei = []
    for i in range (0,num_of_edges):
        verticesInEdge = random.randint(1,max_vertices_per_edge)
        edge = list(np.random.permutation(np.arange(0,num_of_intervals))[:verticesInEdge])
        Ei.append(edge)
    
    return Li,Ri,Ei,Qi,probability_distribution_list

#p= 10 * [1]
#print(minimumProblem(10,10,1,1,p))
#print(hypergraphOrientationProblem(10,8,3,10,1,1,p))
def makeInstance(num_of_intervals,salt):
    li = [0]
    Ri = [10]
    current_point = salt
    for i in range(1,num_of_intervals):
        salt = randomUniform(current_point,current_point+ (10-current_point) *i/num_of_intervals)
        current_point = salt
        li.append(salt)
        Ri.append(salt+10)
    print(li)
    print(Ri)
#makeInstance(10,9.8)