import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp
from simulation import *
import copy

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
    M = []
    i = 0
    # Line 1
    for man_probability in Mi:
        if man_probability >= d:
           M.append(i)
        i = i + 1
    # Line 2
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print('Not')
        return
    newEi = copy.deepcopy(Ei)
    for v in M:
        for edge in range(0,len(newEi)):
            if v in newEi[edge]:
                newEi[edge].remove(v)
    LEi,REi = getEndpoints(newEi)
    print(newEi)
    data = {}
    constrMatrix = []
    for edge in range(0,len(newEi)):
        zero = np.zeros(len(Li))
        zero[LEi[edge]] = 1
        zero[REi[edge]] = 1
        constrMatrix.append(zero)
    print(constrMatrix)
    data['constraint_coeffs'] = constrMatrix
    data['bounds'] = [1] * len(newEi)
    data['obj_coeffs'] = Qi
    data['num_vars'] = len(Qi)
    data['num_constraints'] = len(newEi)
    infinity = solver.infinity()
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.IntVar(0, infinity, 'x[%i]' % j)

    for i in range(data['num_constraints']):
        constraint_expr = [data['constraint_coeffs'][i][j] * x[j] for j in range(data['num_vars'])]
        solver.Add(sum(constraint_expr) >= data['bounds'][i])

    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMinimization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        v1 = []
        for j in range(data['num_vars']):
            if x[j].solution_value() == 1:
                v1.append(j)
        print(v1)
    else:
        print('The problem does not have an optimal solution.')
    print(M)
    querylist = []
    for edge in Ei:
        print(edge)

        for v in edge:
            x = False
            if v in M or v in v1:
                x = True
            querylist.append(x)
            print(Vi[v],x)
        print()
    print(Ei)
    print(querylist)

# Li,Ri,Qi,Pi,Mi,d,Ei,Vi
Li = [8.954043650674025, 12.544740640790216, 16.526478330884725, 23.571122884852443, 24.53476179983959, 29.31006694062271, 30.468548517748523, 34.98627619335313, 41.807224776281615, 46.507874846272344]
Ri = [55.292546691529026, 63.171997468128986, 70.33326216010276, 77.17071823078149, 80.58724735945381, 83.06502423225356, 88.41442538519962, 93.76809603248427, 94.86608777800942, 100.72436167731871]
Qi = [1] * len(Li)
Pi = [1] * len(Li)
Mi = [1,0,0.5,0,0,1,0,0.5,0,0]
d = 0.75
Ei = [[1,2,3],[0,5,7],[3,4,5],[8,9],[0,4,5,6,7],[1,6,9],[4,7],[4,8]]
Vi = minimumProblemSimulation(Li,Ri,Pi)
thresholdAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi)
