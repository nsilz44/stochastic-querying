from probabilities import *
from itertools import permutations
import numpy as np

''' The algorithm to find an approximation to the minimal element problem section 3.1 
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517'''

def approximationAlgorithm(Li,Ri,Qi,Pi,Vi):
    G = []
    n = len(Li)
    wR = (sum(Qi) - Qi[0])
    # R = I[1] -> I[n-1]
    tilt = False
    for j in range(1,n):
        if Qi[j] >= 3/4 * wR:
            tilt = True
            break
    if tilt == True:
        return tilt
    else:
        largest_Q = np.argmax(Qi)
        if wR/2 <= largest_Q and largest_Q <= 3/4 * wR:
            Gprime = largest_Q
        else: #above not true
            workG = 0
            for i in range(1,n-1):
                for Wi in permutations(range(1,n), i):
                    sum = 0
                    for i in Wi:
                        sum += Qi[i]
                    if wR/2 <= sum and sum <= 3/4 * wR:
                        workG = sum
                        break
                if workG != 0:
                    break

# cascade after querying I0 and sometimes previous ones      
def cascade(query_set,Li,Ri,Qi,Pi,Vi):
    min_value = 1000000000000000000000000000000000000000000000000000
    for i in query_set:
        del Li[i]
        del Ri[i]
        del Qi[i]
        del Pi[i]
        if min_value > Vi[i]:
            min_value = Vi[i]
        del Vi[i]
    queries = 0
    while len(Vi) != 0:
        # min value is smallest 
        if min_value < Li[0]:
            break
        if queries in query_set:
            queries += 1
            continue
        else:
            query_set.append(queries)
            del Li[0]
            del Ri[0]
            del Qi[0]
            del Pi[0]
            if min_value > Vi[0]:
                min_value = Vi[0]
            del Vi[0]
            queries += 1 
    return query_set, min_value

def testCascade():
    finhl, lol = cascade([4,2],[1,2,2.5,3,4],[5,6,6.5,7,8],[1,1,1,1,1],[11,1,1,1,1],[3,5,2.6,6,7])
    print(lol)
    print(finhl)
        
testCascade()