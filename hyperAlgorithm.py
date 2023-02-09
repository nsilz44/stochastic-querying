import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp

''' Threshold algorithm for orienting graphs and its generalization to hypergraphs. Section 3.1
Bampis, E., Dürr, C., Erlebach, T., de Lima, M. S., Megow, N., & Schlöter, J. Orienting (hyper) 
graphs under explorable stochastic uncertainty. (2021). https://doi.org/10.4230/LIPIcs.ESA.2021.10
'''
def getEndpoints(Ei):
    LEi = []
    REi = []
    for edge in Ei:
        LEi.append(edge[0])
        REi.append(edge[-1])
    return LEi,REi

# list Li -> list of interval left endpoint
# list Ri -> list of interval right endpoint
# list Qi -> list of query cost per interval
# list Pi -> list of interval probability distribution
# list Mi -> list of vertex being mandatory
# value d -> threshold for approximation ratio of vertex cover
# list of list Ei -> list of lists of hyperedges
# list Vi -> list of realisation of instance
def thresholdAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi):
    LEi,REi = getEndpoints(Ei)
    M = []
    i = 0
    # Line 1
    for man_probability in Mi:
        if man_probability >= d:
           M.append(i)
        i = i + 1
    # Line 2
    
