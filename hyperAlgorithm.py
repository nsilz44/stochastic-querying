import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp
from simulation import *
import copy
import math

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
    for i in range(num_iterations):
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
                    if edgeVi[smallest_index] <= edgeLi[k]:
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
    print(M)
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
    print(newEi)
    LEi,REi = getEndpoints(newEi)
    data = {}
    constrMatrix = []
    for endpoint in range(0,len(LEi)):
        zero = np.zeros(len(Li))
        zero[LEi[endpoint]] = 1
        zero[REi[endpoint]] = 1
        constrMatrix.append(zero)
    print(constrMatrix)
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
    print('Number of constraints =', solver.NumConstraints())
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
        print('v1',v1)
        print('v0.5',v05)
        print('v0',v0)
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
    print('M',M)
    print(querylist)
    print(Ei)
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
    print(Vi)
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
    print(constrMatrix)
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
    print('Number of constraints =', solver.NumConstraints())
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
        print('v1',v1)
        print('v0.5',v05)
        print('v0',v0)
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
    print(querylist)
    print(Ei)
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
    print(Vi)
    return final_query_list

# Li,Ri,Qi,Pi,Mi,d,Ei,Vi
Li = [8.954043650674025, 12.544740640790216, 16.526478330884725, 23.571122884852443, 24.53476179983959, 29.31006694062271, 30.468548517748523, 34.98627619335313, 41.807224776281615, 46.507874846272344]
Ri = [55.292546691529026, 63.171997468128986, 70.33326216010276, 77.17071823078149, 80.58724735945381, 83.06502423225356, 88.41442538519962, 93.76809603248427, 94.86608777800942, 100.72436167731871]
Qi = [1] * len(Li)
Pi = [1] * len(Li)
d = 2 / (1 + math.sqrt(5))
Ei = [[0,1],[1,5],[5,7],[7,9],[0,9]]
Mi = findMandatoryProbabilities(Li,Ri,Qi,Pi,Ei,1000)
Vi = minimumProblemSimulation(Li,Ri,Pi)
print(thresholdLIPAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi))
print(bestVCAlgorithm(Li,Ri,Qi,Pi,Mi,Ei,Vi))



