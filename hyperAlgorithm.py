import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp
from simulation import *
import copy
import math
import time
from optimalQuerySet import *

''' Threshold algorithm for orienting graphs and its generalization to hypergraphs. Section 3.1
Bampis, E., Dürr, C., Erlebach, T., de Lima, M. S., Megow, N., & Schlöter, J. Orienting (hyper) 
graphs under explorable stochastic uncertainty. (2021). https://doi.org/10.4230/LIPIcs.ESA.2021.10
'''
def getEndpoints(Ei):
    LEi = []
    REi = []
    for edge in Ei:
        if len(edge) == 1:
            LEi.append(edge[0])
            REi.append(edge[-1])
        for i in range(1,len(edge)):
            LEi.append(edge[0])
            REi.append(edge[i])
    return LEi,REi

def findMandatoryProbabilities(Li,Ri,Qi,Pi,Ei,num_iterations):
    sum_mandatory_probabilities = [0] * len(Li)
    time_start = time.time()
    for i in range(num_iterations):
        time_finish = time.time()
        if time_finish - time_start >= 3600:
            num_simulations = i
            break
        query_list = []
        Vi = minimumProblemSimulation(Li,Ri,Pi)
        for edge in Ei:
            edgeVi = []
            edgeLi = []
            edgeRi = []
            edgeQi = []
            for v in edge:
                edgeLi.append(Li[v])
                edgeRi.append(Ri[v])
                edgeVi.append(Vi[v])
                edgeQi.append(Qi[v])
            min_value = min(edgeVi)
            for a in range(len(edge)):
                if edgeVi[a] == min_value:
                    smallest_index = a
                    break
            for k in range(len(edge)):
                if k == smallest_index:
                    for j in range(len(edge)):
                        if j == k:
                            continue
                        elif edgeVi[j] <= edgeRi[k]:
                            query_list.append(edge[k])
                            break
                else:
                    if edgeVi[smallest_index] >= edgeLi[k]:
                        query_list.append(edge[k])
        for idx in range(len(Li)):
            if idx in query_list:
                sum_mandatory_probabilities[idx] += 1
    mandatory_probabilities = []
    for idx in sum_mandatory_probabilities:
        mandatory_probabilities.append(idx/num_iterations)
    return mandatory_probabilities


def cascade_edge(querylist,Li,Vi,edge):
    querylist.append(edge[0])
    min_value = Vi[edge[0]]
    for i in range(1,len(edge)):
        if min_value < Li[edge[i]]:
            break
        else:
            querylist.append(edge[i])
            if Vi[edge[i]] < min_value:
                min_value = Vi[edge[i]]
    return querylist

# list Li -> list of interval left endpoint
# list Ri -> list of interval right endpoint
# list Qi -> list of query cost per interval
# list Pi -> list of interval probability distribution
# list Mi -> list of vertex being mandatory
# value d -> threshold for approximation ratio of vertex cover
# list of list Ei -> list of lists of hyperedges
# list Vi -> list of realisation of instance

def thresholdLIPAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi):
    M = []
    i = 0
    # Line 1
    for man_probability in Mi:
        if man_probability >= d:
           M.append(i)
        i = i + 1
    #print(M)
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
    for edge in newEi:
        if len(edge)==0:
            newEi.remove(edge)
    #print(newEi)
    LEi,REi = getEndpoints(newEi)
    data = {}
    constrMatrix = []
    for endpoint in range(0,len(LEi)):
        zero = np.zeros(len(Li))
        zero[LEi[endpoint]] = 1
        zero[REi[endpoint]] = 1
        constrMatrix.append(zero)
    #print(constrMatrix)
    data['constraint_coeffs'] = constrMatrix
    data['bounds'] = [1] * len(LEi)
    data['obj_coeffs'] = Qi
    data['num_vars'] = len(Qi)
    data['num_constraints'] = len(LEi)
    infinity = solver.infinity()
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.IntVar(0, infinity, 'x[%i]' % j)
 
    for i in range(data['num_constraints']):
        constraint_expr = [data['constraint_coeffs'][i][j] * x[j] for j in range(data['num_vars'])]
        solver.Add(sum(constraint_expr) >= data['bounds'][i])
    #print('Number of constraints =', solver.NumConstraints())
    obj_expr = [data['obj_coeffs'][j] * x[j] for j in range(data['num_vars'])]
    solver.Minimize(solver.Sum(obj_expr))

    status = solver.Solve()
    # Line 3
    if status == pywraplp.Solver.OPTIMAL:
        v1 = []
        v05= []
        v0 = []
        for j in range(data['num_vars']):
            if x[j].solution_value() == 1:
                v1.append(j)
            if x[j].solution_value() == 0.5:
                v05.append(j)
            if x[j].solution_value() == 0:
                v0.append(j)
        #print('v1',v1)
        #print('v0.5',v05)
        #print('v0',v0)
    else:
        print('The problem does not have an optimal solution.')
    querylist = []
    #line 5
    for edge in Ei:
        #print(edge)
        for v in edge:
            x = False
            if v in M or v in v1:
                x = True
                querylist.append(v)
            #print(Vi[v],x)
        #print()
    #print('M',M)
    #print(querylist)
    #print(Ei)
    # Line 6
    for edge in Ei:
        if edge[0] in querylist:
            querylist = cascade_edge(querylist,Li,Vi,edge)
        else:
            cascade = False
            for i in range(1,len(edge)):
                if edge[i] in querylist:
                    if Vi[edge[i]] <= Ri[edge[0]]:
                        cascade = True
                        break
            if cascade == True:
                querylist = cascade_edge(querylist,Li,Vi,edge)
            else:
                for i in range(1,len(edge)):
                    if edge[i] not in querylist:
                        querylist.append(edge[i])
                        if Vi[edge[i]] <= Ri[edge[0]]:
                            cascade = True
                            break
                if cascade == True:
                    querylist = cascade_edge(querylist,Li,Vi,edge)
    final_query_list = []
    for idx in range(len(Li)):
        if idx in querylist:
            final_query_list.append(idx)
    #print(Vi)
    return final_query_list


def bestVCAlgorithm(Li,Ri,Qi,Pi,Mi,Ei,Vi):
    # Line 2
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print('Not')
        return
    newEi = copy.deepcopy(Ei) 
    LEi,REi = getEndpoints(newEi)
    data = {}
    constrMatrix = []
    for endpoint in range(0,len(LEi)):
        zero = np.zeros(len(Li))
        zero[LEi[endpoint]] = 1
        zero[REi[endpoint]] = 1
        constrMatrix.append(zero)
    #print(constrMatrix)
    obj_cof = []
    for j in range(len(Qi)):
        obj_cof.append((1-Mi[j])*Qi[j])
    data['constraint_coeffs'] = constrMatrix
    data['bounds'] = [1] * len(LEi)
    data['obj_coeffs'] = obj_cof
    data['num_vars'] = len(Qi)
    data['num_constraints'] = len(LEi)
    infinity = solver.infinity()
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.IntVar(0, infinity, 'x[%i]' % j)
 
    for i in range(data['num_constraints']):
        constraint_expr = [data['constraint_coeffs'][i][j] * x[j] for j in range(data['num_vars'])]
        solver.Add(sum(constraint_expr) >= data['bounds'][i])
    #print('Number of constraints =', solver.NumConstraints())
    obj_expr = [data['obj_coeffs'][j] * x[j] for j in range(data['num_vars'])]
    solver.Minimize(solver.Sum(obj_expr))

    status = solver.Solve()
    # Line 3
    if status == pywraplp.Solver.OPTIMAL:
        v1 = []
        v05= []
        v0 = []
        for j in range(data['num_vars']):
            if x[j].solution_value() == 1:
                v1.append(j)
            if x[j].solution_value() == 0.5:
                v05.append(j)
            if x[j].solution_value() == 0:
                v0.append(j)
        #print('v1',v1)
        #print('v0.5',v05)
        #print('v0',v0)
    else:
        print('The problem does not have an optimal solution.')
    querylist = []
    #line 5
    for edge in Ei:
        #print(edge)
        for v in edge:
            x = False
            if v in v1:
                x = True
                querylist.append(v)
            #print(Vi[v],x)
        #print()
    # Line 6
    for edge in Ei:
        if edge[0] in querylist:
            querylist = cascade_edge(querylist,Li,Vi,edge)
        else:
            cascade = False
            for i in range(1,len(edge)):
                if edge[i] in querylist:
                    if Vi[edge[i]] <= Ri[edge[0]]:
                        cascade = True
                        break
            if cascade == True:
                querylist = cascade_edge(querylist,Li,Vi,edge)
            else:
                for i in range(1,len(edge)):
                    if edge[i] not in querylist:
                        querylist.append(edge[i])
                        if Vi[edge[i]] <= Ri[edge[0]]:
                            cascade = True
                            break
                if cascade == True:
                    querylist = cascade_edge(querylist,Li,Vi,edge)
    final_query_list = []
    for idx in range(len(Li)):
        if idx in querylist:
            final_query_list.append(idx)
    return final_query_list

def queryCalculate(query_set):
    cost = 0
    for query in query_set:
        cost += Qi[query]
    return cost
# Li,Ri,Qi,Pi,Mi,d,Ei,Vi
def testHyper():
    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    d = 2 / (1 + math.sqrt(5)) 
    print(d)
    Mi = findMandatoryProbabilities(Li,Ri,Qi,Pi,Ei,10000)
    print(Mi)
    Vi = minimumProblemSimulation(Li,Ri,Pi)
    q = thresholdLIPAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi)
    print(q,queryCalculate(q))
    q = bestVCAlgorithm(Li,Ri,Qi,Pi,Mi,Ei,Vi)
    print(q,queryCalculate(q))
    q = hypergraphOptimalQuerySet(Li,Ri,Vi,Qi,Ei)
    print(q,queryCalculate(q))

#testHyper()