from probabilities import *
from itertools import permutations
import numpy as np

''' The algorithm to find an approximation to the minimal element problem section 3.1 
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517'''

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

def approximationAlgorithm(Li,Ri,Qi,Pi,Vi):
#   1
    G = []
    n = len(Li)
    wA = np.sum(Qi)
    wR = (wA - Qi[0])
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
        print(m)
        R.remove(costly_j)
        u = calcProbHit(Li,Ri,Pi,R)
        print(u)
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
                        Gprime.extend(Wi)
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
    
    k = 0 
    sumK = 0
    '''while sumK <= wR:
        sumK += Qi[k]
        k += 1
    POne = calcProb(Pi[0],Li[k],Ri[0],Ri[0]-Li[0])
    PR = calcProbHit(Li,Ri,Pi,R)
    R = list(range(1,n))  
    muOne = 1 + (1 - PR) * POne * Qi[0] / wR
    z = wR / Qi[0]
    muR = 1 + (13/16) * z + (1 - PR) * (POne * (1 - z) + 13/16 * z - 1) 
    pOne = 1 + POne * (1 - PR) * Qi[0] / wR
    pR = (1-PR) * POne + PR + (1-POne+(PR*POne/4)) * z + (3*PR*POne/4) * (z/((3*z)+4))
    pPrimeOne = calcProb(Pi[0],Li[costly_j],Ri[0],Ri[0]-Li[0])
    pJ = calcProb(Pi[costly_j],Li[costly_j],Ri[0],Ri[costly_j]-Li[costly_j])
    wRPrime = wR - Qi[costly_j]
    phiOne = pPrimeOne * (pJ *(1+ (wRPrime/(Qi[0]+Qi[costly_j]))) + ((1 - pJ) * (1+(1/z)))) + (1 - pPrimeOne) * (pJ*(1+(wRPrime/Qi[0])) + (1-pJ)*((wRPrime+Qi[0])/min(Qi[0],wR)))
    phiJ = pJ * ((1-pPrimeOne)*(1+z) + pPrimeOne*(1+(wRPrime/(Qi[0]+Qi[costly_j])))) + (1-pJ)*(pPrimeOne + (1-pPrimeOne)* wR / min(Qi[0],wR))
    '''
    muOne = 1
    muR = 0
    pOne = 1
    pR = 0
    phiOne = 1
    phiJ = 0 
    if len(G) != 0:
        print(G)
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
        # case 2
        if Qi[0] <= (3/4) * wR:
            if pOne <= pR:
                query_list = [0]
                query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                return query_list
            else:
                R = list(range(1,n))
                query_list = R.copy()
                for j in R:
                    if Vi[j] <= Ri[0]:
                        query_list.append(0)
                        return query_list
                return query_list
        #case 3
        else:#####check
            query_list = list(range(1,n))
            query_list.remove(costly_j)
            for j in query_list:
                if Vi[j] <= Ri[0]:
                    query_list.append(0)
                    current_min = Vi[0]
                    for v in Vi:
                        if v < current_min:
                            current_min = v
                    if current_min >= Li[costly_j]:
                        query_list.append(costly_j)
                    return query_list
            #case 3.1
            if phiOne <= phiJ:
                query_list.append(0)
                current_min = Vi[0]
                for v in Vi:
                    if v < current_min:
                        current_min = v
                if current_min >= Li[costly_j]:
                    query_list.append(costly_j)
                return query_list
            # case 3.2
            else:
                query_list.append(costly_j)
                current_min = Vi[costly_j]
                for v in Vi:
                    if v < current_min:
                        current_min = v
                if current_min <= Ri[0]:
                    query_list.append(0)
                return query_list

def testSnhit():
    Li = [1,5,6,7]
    Ri = [8,8.5,19,20]
    Qi = [111,10,1,2]
    Vi = [4,7,7,12]
    Pi = ['1','1','1','1']
    print(approximationAlgorithm(Li,Ri,Qi,Pi,Vi))

testSnhit()


def testCascade():
    finhl, lol = cascade([4,2],[1,2,2.5,3,4],[5,6,6.5,7,8],[1,1,1,1,1],[11,1,1,1,1],[3,5,2.6,6,7])
    print(lol)
    print(finhl)
        
#testCascade()