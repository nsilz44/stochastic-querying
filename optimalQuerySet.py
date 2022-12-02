from probabilities import *
from instanceGenerator import *
from simulation import *

''' The algorithm to find optimal query set from section 3 Lemma 6
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517 '''
def minimumProblemOptimalQuerySet(Li,Ri,Vi,Qi):
    n = len(Li)
    min_value = min(Vi)
    i = 0
    query_set = []
    cost = 0
    while Li[i] <= min_value:
        if Ri[i] >= min_value:
            query_set.append(i)
            cost += Qi[i]
        i += 1
        if i == n:
            break
    remove_one = True
    new_cost = 0
    if min_value == Vi[0]:
        for j in range(1,n):
            new_cost += Qi[j]
            if Vi[j] <= Ri[0]:
                remove_one == False
    if remove_one == True and new_cost < cost:
        del query_set[0]
    return query_set

def testOptionA():
    p= 10 * ['1']
    m = minimumProblem(10,10,p,p)
    print('instance: ', m)
    s = minimumProblemSimulation(m[0],m[1],m[3])
    print('simulation: ', s)
    q = minimumProblemOptimalQuerySet(m[0],m[1],s,p)
    print('query set: ', q)
#testOptionA()    

def testOptionB():
    print(minimumProblemOptimalQuerySet([10,11,12,13],[14,17,22,25],[13.5,15,20,22],[12,1,3,5]))
testOptionB()