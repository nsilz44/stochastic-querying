from probabilities import *
from instanceGenerator import *
from simulation import *

''' The algorithm to find optimal query set from section 3 Lemma 6
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517 '''


# ASSUMPTION: Li[0] < Li[1] < ... < Li[n-1] < Ri[0] < Ri[1] < ... < Ri[n-1]
def minimumProblemOptimalQuerySet(Li,Ri,Vi,Qi):
    # Does option a
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
    # Checks whether option B is better
    remove_one = True
    new_cost = sum(Qi) - Qi[0]
    for j in range(1,n):
        new_cost += Qi[j]
        # value which is a mandatory query
        if Vi[j] <= Ri[0]:
            remove_one == False
            break
    if remove_one == True and new_cost < cost:
        query_set = list(range(1,(n)))
    return query_set

def testOptionA():
    p= 10 * ['1']
    l = 10 * [1]
    m = minimumProblem(5,5,p,l)
    print('instance: ', m)
    s = minimumProblemSimulation(m[0],m[1],m[2])
    print('simulation: ', s)
    q = minimumProblemOptimalQuerySet(m[0],m[1],s,l)
    print('query set: ', q)
#testOptionA()    

def testOptionB():
    print(minimumProblemOptimalQuerySet([10,11,12,13],[14,17,22,25],[13.5,15,20,22],[12,1,3,5]))
    print(minimumProblemOptimalQuerySet([0,4,4.5,6],[10,20,21,22],[5,12,13,12],[5,1,1,1]))
    print(minimumProblemOptimalQuerySet([0,2,6],[10,12,14],[5,4,12],[1,1,10]))
#testOptionB()