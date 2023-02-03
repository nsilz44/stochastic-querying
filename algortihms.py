from probabilities import *
from itertools import permutations
import numpy as np
from simulation import *

''' The algorithm to find an approximation to the minimal element problem section 3.1 
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517'''

# Calculate probability of a least 1 value hitting I0
def calcProbHit(Li,Ri,Pi,list_hit):
    missing_probability = 1
    for j in list_hit:
        miss = calcProb(Pi[j],Ri[0],Ri[j],(Ri[j]-Li[j]))
        #if miss > 1:
            #print(Pi[j],Ri[0],Ri[j],(Ri[j]-Li[j]))
        missing_probability = missing_probability * miss
    return 1 - missing_probability

# cascade after querying I0 and sometimes previous ones      
def cascade(query_set,Li,Ri,Qi,Pi,Vi):
    min_value = 1000000000000000000000000000000000000000000000000000
    copy_Li = Li.copy()
    copy_Ri = Ri.copy()
    copy_Qi = Qi.copy()
    copy_Pi = Pi.copy()
    copy_Vi = Vi.copy()
    j = 0
    for i in query_set:
        #print(i,j,copy_Vi,Vi)
        del copy_Li[(i-j)%len(copy_Li)]
        del copy_Ri[(i-j)%len(copy_Li)]
        del copy_Qi[(i-j)%len(copy_Qi)]
        del copy_Pi[(i-j)%len(copy_Pi)]
        if min_value > Vi[i-j]:
            min_value = Vi[i-j]
        del copy_Vi[(i-j)%len(copy_Vi)]
        j = j + 1
    queries = 0
    #print(copy_Li,copy_Vi)
    while len(copy_Vi) != 0:
        # min value is smallest 
        if min_value < copy_Li[0]:
            break
        if queries in query_set:
            queries += 1
            continue
        else:
            query_set.append(queries)
            del copy_Li[0]
            del copy_Ri[0]
            del copy_Qi[0]
            del copy_Pi[0]
            if min_value > copy_Vi[0]:
                min_value = copy_Vi[0]
            del copy_Vi[0]
            queries += 1
    #print(query_set) 
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
    while sumK <= wR:
        sumK = sumK + Qi[k]
        k = k + 1
    POne = calcProb(Pi[0],Li[k-1],Ri[0],Ri[0]-Li[0])
    R = list(range(1,n)) 
    PR = calcProbHit(Li,Ri,Pi,R)
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
    
    if len(G) != 0:
        #print('case 1')
        if muOne <= muR:
            query_list = [0]
            query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
            return query_list
        else:
            #print('case 1.2')
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
        #print('case 2')
        if Qi[0] <= (3/4) * wR:
            #print(pOne,pR)
            if pOne <= pR:
                query_list = [0]
                query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                return query_list
            else:
                R = list(range(1,n))
                query_list = []
                for j in R:
                    query_list.append(j)
                    if Vi[j] <= Ri[0]:
                        query_list.append(0)
                        query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                        print(query_list)
                        return query_list
                return query_list
        else:#####check
            query_list = []
            R = list(range(1,n))
            R.remove(costly_j)
            #print(R)
            for j in R:
                query_list.append(j)
                if Vi[j] <= Ri[0]:
                    query_list.append(0)
                    query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
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




def testCascade():
    finhl, lol = cascade([4,2,0],[1,2,2.5,3,4],[5,6,6.5,7,8],[1,1,1,1,1],[11,1,1,1,1],[3,5,2.6,6,7])
    print(lol)
    print(finhl)
        
#testCascade()

# heuristic - Case 1 queries highest chance / querycost of R hitting I0
def heuristicOneApproximationAlgorithm(Li,Ri,Qi,Pi,Vi):
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
    while sumK <= wR:
        sumK += Qi[k]
        k += 1
    POne = calcProb(Pi[0],Li[k-1],Ri[0],Ri[0]-Li[0])
    R = list(range(1,n)) 
    PR = calcProbHit(Li,Ri,Pi,R) 
    muOne = 1 + (1 - PR) * POne * Qi[0] / wR
    z = wR / Qi[0]
    muR = 1 + (13/16) * z + (1 - PR) * (POne * (1 - z) + 13/16 * z - 1) 
    pOne = 1 + POne * (1 - PR) * Qi[0] / wR
    pR = (1-PR) * POne + PR + (1-POne+(PR*POne/4)) * z + (3*PR*POne/4) * (z/((3*z)+4))
    #print(pOne,pR)
    pPrimeOne = calcProb(Pi[0],Li[costly_j],Ri[0],Ri[0]-Li[0])
    pJ = calcProb(Pi[costly_j],Li[costly_j],Ri[0],Ri[costly_j]-Li[costly_j])
    wRPrime = wR - Qi[costly_j]
    phiOne = pPrimeOne * (pJ *(1+ (wRPrime/(Qi[0]+Qi[costly_j]))) + ((1 - pJ) * (1+(1/z)))) + (1 - pPrimeOne) * (pJ*(1+(wRPrime/Qi[0])) + (1-pJ)*((wRPrime+Qi[0])/min(Qi[0],wR)))
    phiJ = pJ * ((1-pPrimeOne)*(1+z) + pPrimeOne*(1+(wRPrime/(Qi[0]+Qi[costly_j])))) + (1-pJ)*(pPrimeOne + (1-pPrimeOne)* wR / min(Qi[0],wR))
    
    if len(G) != 0:
        if muOne <= muR:
            query_list = [0]
            query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
            return query_list
        else: 
            query_list = []
            newG = [0]
            for i in R:
                hit_per_cost = calcProbHit(Li,Ri,Pi,[i])/Qi[i]
                newG.append(hit_per_cost)
            R = np.argsort(newG)
            R = np.flip(R)
            R = R[:-1]
            for i in R:
                query_list.append(i)
                if Vi[i] <= Ri[0]:
                    query_list.append(0)
                    if len(query_list) != len(Li):
                    #print(query_list)
                        query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
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
                query_list = []
                newG = [0]
                for i in R:
                    hit_per_cost = calcProbHit(Li,Ri,Pi,[i])/Qi[i]
                    newG.append(hit_per_cost)
                R = np.argsort(newG)
                R = np.flip(R)
                R = R[:-1]
                for i in R:
                    query_list.append(i)
                    if Vi[i] <= Ri[0]:
                        query_list.append(0)
                        if len(query_list) != len(Li):
                        #print(query_list)
                            query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                        return query_list
                return query_list
        #case 3
        else:
            query_list = []
            newG = [0]
            for i in R:
                hit_per_cost = calcProbHit(Li,Ri,Pi,[i])/Qi[i]
                newG.append(hit_per_cost)
            R = np.argsort(newG)
            R = np.flip(R)
            R = R[:-1]
            for i in R:
                query_list.append(i)
                if Vi[i] <= Ri[0]:
                    query_list.append(0)
                    if len(query_list) != len(Li):
                    #print(query_list)
                        query_list , min_value = cascade(query_list,Li,Ri,Qi,Pi,Vi)
                    return query_list
            return query_list  

def testhit():
    Li = [0, 9.815421312880146, 9.843662412508552, 9.84528093866387, 9.905831711422326, 9.907239868130803, 9.941693807153053, 9.982184977950723, 9.982616317462947, 9.983592476481835]
    Ri = [10, 19.815421312880147, 19.84366241250855, 19.84528093866387, 19.905831711422326, 19.9072398681308, 19.94169380715305, 19.982184977950723, 19.98261631746295, 19.983592476481835]
    Qi = [45,28,1,1,6,2,1,3,1,1]
    Pi = [1] * len(Li)
    Vi = minimumProblemSimulation(Li,Ri,Pi)
    print(approximationAlgorithm(Li,Ri,Qi,Pi,Vi))
#testhit()