from probabilities import *
from instanceGenerator import *
from simulation import *
def minimumProblemUniformOptimalQuerySet(Li,Ri,Vi):
    n = len(Li)
    min_value = min(Vi)
    i = 0
    query_set = []
    while Li[i] <= min_value:
        if Ri[i] >= min_value:
            query_set.append(i)
        i += 1
    if len(query_set) == n:
        query_set.remove(0)
    return query_set

'''p= 10 * ['1']
m = minimum_problem(10,10,1,0,p)
print(m)
s = minimumProblemSimulation(m[0],m[1],m[3])
print(s)
q = minimumProblemUniformOptimalQuerySet(m[0],m[1],s)
print(q)'''    