import random

# 
def minimum_problem(num_of_intervals,salt_max,query_cost_uniformness,query_cost_max,probability_distribution_list):
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
    
    if query_cost_uniformness == 1:
        Qi = [query_cost_max] * num_of_intervals
    return Li,Ri,Qi,probability_distribution_list

#p= 10 * [1]
#print(minimum_problem(10,10,1,1,p))
