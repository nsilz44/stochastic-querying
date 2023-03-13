import random
from scipy.stats import beta
from scipy.stats import semicircular
from scipy.stats import gausshyper
from scipy.stats import rdist
from scipy.stats import bradford
import matplotlib.pyplot as plt
import numpy as np


def uniformProb(l_endpoint,r_endpoint):
    return random.uniform(l_endpoint,r_endpoint)

def calcUniformProb(l_endpoint,r_endpoint,range):
    return (r_endpoint - l_endpoint)/range 

def semiCircularProb(l_endpoint,r_endpoint):
    r = semicircular.rvs(size=1)
    return l_endpoint + (r[0]+1)/2 * (r_endpoint-l_endpoint)

def betaProb(l_endpoint,r_endpoint):
    a, b = 2, 0.8
    r = beta.rvs(a, b, size=1)
    return l_endpoint + r[0] * (r_endpoint-l_endpoint)

def gausshyperProb(l_endpoint,r_endpoint):
    a, b, c, z = 10, 3, 2, 5
    r = gausshyper.rvs(a, b, c, z, size=1)
    return l_endpoint + r[0] * (r_endpoint-l_endpoint)

def rdistProb(l_endpoint,r_endpoint):
    c = 1.6
    r = rdist.rvs(c,size=1)
    return l_endpoint + (r[0]+1)/2 * (r_endpoint-l_endpoint)

def bradfordProb(l_endpoint,r_endpoint):
    c = 10
    r = bradford.rvs(c,size=1)
    return l_endpoint + r[0] * (r_endpoint-l_endpoint)

betaA, betaB = 2, 0.8
betaRv = beta(betaA, betaB)
def calcBetaProb(l_endpoint,r_endpoint,range):
    return(betaRv.cdf((r_endpoint - l_endpoint)/range))

semiRv = semicircular()
def calcSemiCircularProb(l_endpoint,r_endpoint,range):
    
    return(semiRv.cdf(((r_endpoint - l_endpoint)/range)*2 -1))

gaussA,gaussB,gaussC,gaussZ = 10, 3, 2, 5
gaussRv = gausshyper(gaussA,gaussB,gaussC,gaussZ)

def calcGausshyperProb(l_endpoint,r_endpoint,range):
    return(gaussRv.cdf((r_endpoint - l_endpoint)/range))

rDistC = 1.6
rDistRv = rdist(rDistC)
def calcRdistProb(l_endpoint,r_endpoint,range):
    return(rDistRv.cdf(((r_endpoint - l_endpoint)/range)*2 -1))

bradfordC = 15
bradfordRv = bradford(bradfordC)
def calcBradfordProb(l_endpoint,r_endpoint,range):
    return(bradfordRv.cdf((r_endpoint - l_endpoint)/range))

def prob(probability_type,l_endpoint,r_endpoint):
    if probability_type == 1:
        r = uniformProb(l_endpoint,r_endpoint)
    elif probability_type == 2:
        r = betaProb(l_endpoint,r_endpoint)
    elif probability_type == 3:
        r = semiCircularProb(l_endpoint,r_endpoint)
    elif probability_type == 4:
        r = gausshyperProb(l_endpoint,r_endpoint)
    elif probability_type == 5:
        r = rdistProb(l_endpoint,r_endpoint)
    elif probability_type == 6:
        r = bradfordProb(l_endpoint,r_endpoint)
    return r

def calcProb(probability_type,l_endpoint,r_endpoint,range):
    if probability_type == 1:
        r = calcUniformProb(l_endpoint,r_endpoint,range)
    elif probability_type == 2:
        r = calcBetaProb(l_endpoint,r_endpoint,range)
    elif probability_type == 3:
        r = calcSemiCircularProb(l_endpoint,r_endpoint,range)
    elif probability_type == 4:
        r = calcGausshyperProb(l_endpoint,r_endpoint,range)
    elif probability_type == 5:
        r = calcRdistProb(l_endpoint,r_endpoint,range)
    elif probability_type == 6:
        r = calcBradfordProb(l_endpoint,r_endpoint,range)
    return r

#print(prob(6,10,20))
#print(calcProb(6,10,20,20))
#print(calcProb(1,10,20,20))