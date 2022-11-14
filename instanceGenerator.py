import random

# 
def minimum_problem(num_of_intervals,salt_max,query_cost_uniformness,query_cost_max,probability_distribution):
    Li = []
    current_point = 0
    for i in range (0,num_of_intervals):
        salt = random.uniform(0,salt_max)
        current_point += salt
        Li.append(current_point)
    Ri =[]
    for i in range (0,num_of_intervals):
        salt = random.uniform(0,salt_max)
        current_point += salt
        Ri.append(current_point)
    print(Li)
    print(Ri)
minimum_problem(10,10,0,0,0)
