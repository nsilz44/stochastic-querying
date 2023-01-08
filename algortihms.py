from probabilities import *
from itertools import permutations
import numpy as np

''' The algorithm to find an approximation to the minimal element problem section 3.1 
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517'''

def approximationAlgorithm(Li,Ri,Qi,Pi,Vi):
#   1
    G = []
    n = len(Li)
    wR = (sum(Qi) - Qi[0])
    # R = I[1] -> I[n-1]
    costly = False
    costly_j = 0
    for j in range(1,n):
        if Qi[j] >= 3/4 * wR:
            costly = True
            costly_j = j
            break
    if costly == True:
        #pr[r hits I[0]] = 1 - pr[r not hit I[0]] = for r[j], product of (I[j] missing I[0] = calcProb(Pi[j],Ri[0],Ri[j],size of I[j]))
        R = list(range(1,n))
        m = calcProbHit(Li,Ri,Pi,R)
        R.remove(costly_j)
        u = calcProbHit(Li,Ri,Pi,R)
        if u >= m/4:
            G = R.copy()
    else:
        largest_Q = np.argmax(Qi)
        if wR/2 <= largest_Q and largest_Q <= 3/4 * wR:
            Gprime = largest_Q
        else: #above not true
            workG = 0
            Gprime = []
            for i in range(1,n-1):
                for Wi in permutations(range(1,n), i):
                    sum = 0
                    for i in Wi:
                        sum += Qi[i]
                    if wR/2 <= sum and sum <= 3/4 * wR:
                        workG = sum
                        Gprime = Wi
                        break
                if workG != 0:
                    break
            beta = workG / wR
            primeHit = calcProbHit(Li,Ri,Pi,Gprime)
            R = list(range(1,n))
            m = calcProbHit(Li,Ri,Pi,R)
            if primeHit >= beta * m:
                G = Gprime.copy()
            else:
                for i in Gprime:
                    R.remove(i)
                G = R 
    muOne = 0
    muR = 0
    pOne = 0
    pR = 0
    phiOne = 0
    phiR = 0  
    if len(G) != 0:
        if muOne <= muR:
            query_list = [0]
            query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
            return query_list
        else:
            #query G
            query_list = G.copy()
            for i in G:
                if Vi[i] <= Ri[0]:
                    query_list.append(0)
                    query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                    return query_list
            # else  
            RNotG = list(range(1,n))
            for i in G:
                RNotG.remove(i)
            # query RnotG
            query_list.extend(RNotG)
            for j in RNotG:
                if Vi[j] <= Ri[0]:
                    query_list.append(0)
                    return query_list
            return query_list  
    else:
        if Qi[0] <= (3/4) * wR:
            if pOne <= pR:
                query_list = [0]
                query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                return query_list
            else:
                R = list(range(1,n))
                for j in R:
                    if Vi[j] <= Ri[0]:
                        query_list.append(0)
                        return query_list
                return query_list
        else:
            query_list = list(range(1,n))
            query_list.remove(costly_j)
            for j in query_list:
                if Vi[j] <= Ri[0]:
                    query_list.append(0)
                    if min(Vi[query_list]) >= Li(costly_j):
                        query_list.append(costly_j)
                    return query_list
            if phiOne <= phiR:
                query_list.append(0)
                if min(Vi[query_list]) >= Li(costly_j):
                    query_list.append(costly_j)
                return query_list
            else:
                query_list.append(costly_j)
                if min(Vi[query_list]) <= Ri(0):
                    query_list.append(0)
                return query_list




def calcProbHit(Li,Ri,Pi,list_hit):
    missing_probability = 1
    for j in list_hit:
        miss = calcProb(Pi[j],Ri[0],Ri[j],(Ri[j]-Li[j]))
        missing_probability = missing_probability * miss
    return 1 - missing_probability

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
        
#testCascade()