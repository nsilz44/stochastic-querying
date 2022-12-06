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
        if 
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
        

