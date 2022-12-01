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
    remove_one = False
    if len(query_set) == n:
        remove_one = True
        for v in Vi:
            if v == Vi[0]:
                continue
            if v <= Ri[0]:
                remove_one = False
                break
    if remove_one == True:
        del query_set[0]
    return query_set

def test():
    p= 10 * ['1']
    m = minimumProblem(10,10,p,p)
    print('instance: ', m)
    s = minimumProblemSimulation(m[0],m[1],m[3])
    print('simulation: ', s)
    q = minimumProblemUniformOptimalQuerySet(m[0],m[1],s)
    print('query set: ', q)
#test()    