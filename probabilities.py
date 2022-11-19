import random

def uniform_prob(l_endpoint,r_endpoint):
    return random.uniform(l_endpoint,r_endpoint)

def prob(probability_type,L_endpoint,r_endpoint):
    switch={
    '1': uniform_prob(L_endpoint,r_endpoint),
       }
    return switch.get(probability_type,'not available')

#print(prob('1',10,20))