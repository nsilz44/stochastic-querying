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

def calcBetaProb(l_endpoint,r_endpoint,range):
    a, b = 2, 0.8
    rv = beta(a, b)
    return(rv.cdf((r_endpoint - l_endpoint)/range))

def calcSemiCircularProb(l_endpoint,r_endpoint,range):
    rv = semicircular()
    return(rv.cdf(((r_endpoint - l_endpoint)/range)*2 -1))

def calcGausshyperProb(l_endpoint,r_endpoint,range):
    a, b, c, z = 10, 3, 2, 5
    rv = gausshyper(a,b,c,z)
    return(rv.cdf((r_endpoint - l_endpoint)/range))

def calcRdistProb(l_endpoint,r_endpoint,range):
    c = 1.6
    rv = rdist(c)
    return(rv.cdf(((r_endpoint - l_endpoint)/range)*2 -1))

def calcBradfordProb(l_endpoint,r_endpoint,range):
    c = 15
    rv = bradford(c)
    return(rv.cdf((r_endpoint - l_endpoint)/range))

def prob(probability_type,l_endpoint,r_endpoint):
    switch={
    1: uniformProb(l_endpoint,r_endpoint),
    2: betaProb(l_endpoint,r_endpoint),
    3: semiCircularProb(l_endpoint,r_endpoint),
    4: gausshyperProb(l_endpoint,r_endpoint),
    5: rdistProb(l_endpoint,r_endpoint),
    6: bradfordProb(l_endpoint,r_endpoint),
       }
    return switch.get(probability_type,'not available')

def calcProb(probability_type,l_endpoint,r_endpoint,range):
    switch={
    1: calcUniformProb(l_endpoint,r_endpoint,range),
    2: calcBetaProb(l_endpoint,r_endpoint,range),
    3: calcSemiCircularProb(l_endpoint,r_endpoint,range),
    4: calcGausshyperProb(l_endpoint,r_endpoint,range),
    5: calcRdistProb(l_endpoint,r_endpoint,range),
    6: calcBradfordProb(l_endpoint,r_endpoint,range)
       }
    return switch.get(probability_type,'not available')

#print(prob(6,10,20))
#print(calcProb(6,10,20,20))
#print(calcProb(1,10,20,20))