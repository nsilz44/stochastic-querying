import random
import numpy as np
import networkx as nx

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
        verticesInEdge = random.randint(2,max_vertices_per_edge)
        edge = list(np.random.permutation(np.arange(0,num_of_intervals))[:verticesInEdge])
        edge.sort()
        Ei.append(edge)
    print('Li =',Li)
    print('Ri =',Ri)
    print('Qi =',Qi)
    print('Pi =',probability_distribution_list)
    print('Ei =',Ei)

#print(minimumProblem(10,10,1,1,p))
#hypergraphOrientationProblem(20,40,5,10,[1]*20,[1]*20)


def makeInstance(num_of_intervals,salt):
    li = [0]
    Ri = [10]
    current_point = salt
    for i in range(1,num_of_intervals):
        salt = randomUniform(current_point,current_point+ (10-current_point) *i/num_of_intervals)
        current_point = salt
        li.append(salt)
        Ri.append(salt+10)
    print('Li =',li)
    print('Ri =',Ri)
#makeInstance(100,9.5)

def bipartiteInstance(num_of_intervals,salt_max,Qi,Pi,n,m,p):
    Li,Ri,Qi,Pi = minimumProblem(num_of_intervals,salt_max,Qi,Pi)
    G = nx.bipartite.random_graph(n,m,p)
    Ei = [list(e) for e in G.edges]
    print('Li =',Li)
    print('Ri =',Ri)
    print('Qi =',Qi)
    print('Pi =',Pi)
    print('Ei =',Ei)

#bipartiteInstance(16,10,[1]*16,[1]*16,8,8,0.5)

def pathInstance(num_of_intervals,salt_max,Qi,Pi):
    Li,Ri,Qi,Pi = minimumProblem(num_of_intervals,salt_max,Qi,Pi)
    G = nx.path_graph(num_of_intervals)
    Ei = [list(e) for e in G.edges]
    print('Li =',Li)
    print('Ri =',Ri)
    print('Qi =',Qi)
    print('Pi =',Pi)
    print('Ei =',Ei)

#pathInstance(20,10,[1]*20,[1]*20)
#hypergraphOrientationProblem(20,15,5,10,[1]*20,[1]*20)

def hypergraphOrientationUniformProblem(num_of_intervals,num_of_edges,vertices_per_edge,salt_max,Qi,probability_distribution_list):
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
        verticesInEdge = vertices_per_edge
        edge = list(np.random.permutation(np.arange(0,num_of_intervals))[:verticesInEdge])
        edge.sort()
        Ei.append(edge)
    print('Li =',Li)
    print('Ri =',Ri)
    print('Qi =',Qi)
    print('Pi =',probability_distribution_list)
    print('Ei =',Ei)

#hypergraphOrientationUniformProblem(20,20,6,10,[1]*20,[1]*20)

def randomRegularGraph(d,num_of_intervals,salt_max,Qi,Pi):
    Li,Ri,Qi,Pi = minimumProblem(num_of_intervals,salt_max,Qi,Pi)
    G = nx.random_regular_graph(d, num_of_intervals)
    Ei = [list(e) for e in G.edges]
    for edge in Ei:
        edge.sort()
    print('Li =',Li)
    print('Ri =',Ri)
    print('Qi =',Qi)
    print('Pi =',Pi)
    print('Ei =',Ei)

#randomRegularGraph(2,20,10,[1]*20,[1]*20)

def gnmRandomGraph(m,num_of_intervals,salt_max,Qi,Pi):
    Li,Ri,Qi,Pi = minimumProblem(num_of_intervals,salt_max,Qi,Pi)
    G = nx.gnm_random_graph(num_of_intervals, m, seed=None, directed=False)
    Ei = [list(e) for e in G.edges]
    print('Li =',Li)
    print('Ri =',Ri)
    print('Qi =',Qi)
    print('Pi =',Pi)
    print('Ei =',Ei)

#gnmRandomGraph(30,20,10,[1]*20,[1]*20)