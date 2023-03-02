from probabilities import *
from instanceGenerator import *
from simulation import *

''' The algorithm to find optimal query set from section 3 Lemma 6
Chaplick, S., Halldórsson, M. M., de Lima, M. S., & Tonoyan, T. (2021). 
Query minimization under stochastic uncertainty. Theoretical Computer Science, 
895, 75-95. https://doi.org/10.48550/arXiv.2010.03517 '''


# ASSUMPTION: Li[0] < Li[1] < ... < Li[n-1] < Ri[0] < Ri[1] < ... < Ri[n-1]
def minimumProblemOptimalQuerySet(Li,Ri,Vi,Qi):
    # Does option a
    n = len(Li)
    min_value = min(Vi)
    i = 0
    query_set = []
    cost = 0
    #print(Li[i],min_value,type(Li[i]),type(min_value))

    while Li[i] <= min_value:
        if Ri[i] >= min_value:
            query_set.append(i)
            cost += Qi[i]
        i += 1
        if i == n:
            break
    # Checks whether option B is better
    remove_one = True
    new_cost = sum(Qi) - Qi[0]
    for j in range(1,n):
        # value which is a mandatory query against the first interval
        if Vi[j] <= Ri[0]:
            remove_one = False
            break
    #checks option c happens (query all)
    if (remove_one == True) and (new_cost < cost):
        query_set = list(range(1,n))
    min_value_index = [i for i, value in enumerate(Vi) if value == min_value]
    return min_value_index, query_set

def testOptionA():
    p= 10 * [1]
    l = 10 * [1]
    m = minimumProblem(5,5,p,l)
    print('instance: ', m)
    s = minimumProblemSimulation(m[0],m[1],m[2])
    print('simulation: ', s)
    q = minimumProblemOptimalQuerySet(m[0],m[1],s,l)
    print('query set: ', q)
#testOptionA()    

def testOptionB():
    print(minimumProblemOptimalQuerySet([10,11,12,13],[14,17,22,25],[13.5,15,20,22],[12,1,3,5]))
    print(minimumProblemOptimalQuerySet([0,4,4.5,6],[10,20,21,22],[5,12,13,12],[5,1,1,1]))
    print(minimumProblemOptimalQuerySet([0,2,6],[10,12,14],[4,4,12],[1,1,10]))
#testOptionB()

def cascadeEdge(querylist,Li,Vi,edge):
    querylist.append(edge[0])
    min_value = Vi[edge[0]]
    for i in range(1,len(edge)):
        if min_value < Li[edge[i]]:
            break
        else:
            querylist.append(edge[i])
            if Vi[edge[i]] < min_value:
                min_value = Vi[edge[i]]
    return querylist

def queryRight(Ri,Vi,edge):
    idx_zero_right_endpoint = Ri[edge[0]]
    query_set = []
    for i in range(1,len(edge)):
        if idx_zero_right_endpoint >= Vi[edge[i]]:
            return []
        else:
            query_set.append(edge[i])
    return query_set
def hypergraphOptimalQuerySet(Li,Ri,Vi,Qi,Ei):
    # empty list
    query_sets = [[]]
    for edge in Ei:
        new_query_sets = []
        # additions to query
        cascade_query_set = cascadeEdge([],Li,Vi,edge)
        right_query_set = queryRight(Ri,Vi,edge)
        # loops over all current viable queries
        for query_set in query_sets:
            new_query_set = query_set.copy()
            for query in cascade_query_set:
                if query not in query_set:
                    new_query_set.append(query)
            # ensures all query sets in list are sorted
            new_query_set.sort()
            # adds unique lists to avoid duplicates
            if new_query_set not in new_query_sets:
                new_query_sets.append(new_query_set)
            new_query_set = query_set.copy()
            # same for the right queries
            if right_query_set != []:
                for query in right_query_set:
                    if query not in query_set:
                        new_query_set.append(query)
                # ensures all query sets in list are sorted
                new_query_set.sort()
                if new_query_set not in new_query_sets:
                    new_query_sets.append(new_query_set)
        query_sets = new_query_sets
        #print(edge,query_sets,cascade_query_set,right_query_set)
    min_cost = 10000000000000000000000000000000000000000000000000000000000000000
    best_query_set = []
    print(query_sets)
    for query_set in query_sets:
        cost = 0
        for query in query_set:
            cost += Qi[query]
        if cost < min_cost:
            min_cost = cost
            best_query_set = query_set.copy()
    return best_query_set,min_cost




Li = [8.954043650674025, 12.544740640790216, 16.526478330884725, 23.571122884852443, 24.53476179983959, 29.31006694062271, 30.468548517748523, 34.98627619335313, 41.807224776281615, 46.507874846272344]
Ri = [55.292546691529026, 63.171997468128986, 70.33326216010276, 77.17071823078149, 80.58724735945381, 83.06502423225356, 88.41442538519962, 93.76809603248427, 94.86608777800942, 100.72436167731871]
Qi = [1] * len(Li)
Pi = [1] * len(Li)
Ei = [[0,3],[3,5],[5,7],[0,9],[1,3],[4,6],[1,8],[1,9],[0,8],[1,6,7],[0,4],[5,9]]
Vi = minimumProblemSimulation(Li,Ri,Pi)
print(hypergraphOptimalQuerySet(Li,Ri,Vi,Qi,Ei))
