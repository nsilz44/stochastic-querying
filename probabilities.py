import random

def uniformProb(l_endpoint,r_endpoint):
    return random.uniform(l_endpoint,r_endpoint)

def calcUniformProb(L_endpoint,r_endpoint,range):
    return (r_endpoint - L_endpoint)/range 

def prob(probability_type,L_endpoint,r_endpoint):
    switch={
    1: uniformProb(L_endpoint,r_endpoint),
       }
    return switch.get(probability_type,'not available')

def calcProb(probability_type,L_endpoint,r_endpoint,range):
    switch={
    1: calcUniformProb(L_endpoint,r_endpoint,range),
       }
    return switch.get(probability_type,'not available')
#print(prob('1',10,20))
#print(calcProb('1',10,20,15))