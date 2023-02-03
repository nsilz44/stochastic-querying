from probabilities import *
from instanceGenerator import *
from simulation import *
from optimalQuerySet import *
from algortihms import *
import pandas as pd
import time
import itertools
import seaborn as sns
import matplotlib.pyplot as plt

def start(a):
    if a == 1:
        print('Not a problem')
    print('Type in the problem you would like to test')
    print('Type "m" for the smallest element problem')
    print('Type "s" for the sorting problem')
    print('Type "h" for the hypergraph orientation problem')
    problem = input('')
    if problem == 'm':
        Li,Ri,Qi,Pi = makeMinimumProblem(0)
        doMinimumProblem(Li,Ri,Qi,Pi)
    elif problem == 's':
        sortingProblem()
    elif problem == 'h':
        hypergraphOrientationProblem()
    else:
        start(1)


def doMinimumProblem(Li,Ri,Qi,Pi):
    print('Would you like test this instance or test an algorithm ')
    print('Type i for testing the instance')
    print('Type a for testing the algorithm')
    print('Type s to go back to start')
    instance = input('')
    if instance == 'i':
        testMinInstance(Li,Ri,Qi,Pi)
        doMinimumProblem(Li,Ri,Qi,Pi)
    elif instance == 'a':
        testMinAlgorithm(Li,Ri,Qi,Pi)
    elif instance == 's':
        start(0)
    else:
        print('not i or a typed')
        print('try again')
        doMinimumProblem(Li,Ri,Qi,Pi)

def testMinInstance(Li,Ri,Qi,Pi):
    num_simulations = int(input('How many simulations would you like to test? '))
    min_index_list = []
    query_list = []
    for k in range(0,num_simulations):
        Vi = minimumProblemSimulation(Li,Ri,Pi)
        minimal_index, query_set = minimumProblemOptimalQuerySet(Li,Ri,Vi,Qi)
        min_index_list.append(minimal_index)
        query_list.append(query_set)
    min_index = list(itertools.chain(*min_index_list))
    queries = list(itertools.chain(*query_list))
    print(min_index)
    print(queries)
    return

def makeMinimumProblem(a):
    if a == 1:
        print('Try again')
    print('Type "i" to import an instance')
    print('Type "n" to create a new instance')
    instance = input('')
    if instance == 'i':
        print('Type in the csv filename with the previous instance')
        csvFile = input('')
        path = 'instances/minimumElement/'
        fullpath = path + csvFile
        df = pd.read_csv(fullpath)
        Li = df['Li']
        print(Li)
        Ri = df['Ri']
        print(Ri)
        Qi = df['Qi']
        Pi = df['Pi']
        print(type(Li[0]))
    elif instance == 'n':
        Li,Ri,Qi,Pi = createInstanceMinimumProblem()
    else:
        makeMinimumProblem(1)
    return Li,Ri,Qi,Pi

def createInstanceMinimumProblem():
    intervals = False
    while not intervals:
        try:
            num_of_intervals = int(input('How many intervals would you like? '))
            if num_of_intervals > 0:
                intervals = True
            else:
                print("Try again ")
        except ValueError:
            print("Try again ")
    salt = False
    while not salt:
        try:
            salt_max = float(input('What max salt would you like? '))
            if salt_max > 0:
                salt = True
            else:
                print("Try again ")
        except ValueError:
            print("Try again ")
    uniform = False
    while not uniform:
        print('Would you like uniform queries?')
        uniformness = input('Type in y or n: ') 
        if uniformness == ('y' or 'n'):
            uniform = True
        else:
            print("Try again ")
    if uniformness == 'y':
        uniformness = 1
        max_query = False
        while not max_query:
            try:
                query = float(input('What would you like the query amount to be? '))
                if query > 0:
                    max_query = True
                else:
                    print("Try again ")
            except ValueError:
                print("Try again ")
    else: 
        '''TO be made'''
    Qi = [query] * num_of_intervals
    uniform_prob = False
    while not uniform_prob:
        print('Would you like uniform probabilities?')
        uniformness_prob = input('Type in y or n: ') 
        if uniformness_prob == ('y' or 'n'):
            uniform_prob = True
        else:
            print("Try again ")
    if uniformness_prob == 'y':
        prob = False
        while not prob:
            print('Which probability would you like to use')
            prob_dist = input('Type 1 ') 
            if prob_dist == ('1'):
                prob = True
            else:
                print("Try again ")
        probability_distribution_list = [prob_dist] * num_of_intervals

    else: 
        '''TO be made'''
    Li,Ri,Qi,Pi = minimumProblem(num_of_intervals,salt_max,Qi,probability_distribution_list)
    instance = {    'Li':Li,
                    'Ri':Ri,
                    'Qi':Qi,
                    'Pi':Pi}
    df = pd.DataFrame(instance)
    path = 'instances/minimumElement/'
    filename = path + str(random.randint(0,10000)) + str(num_of_intervals) +'-'+ str(int(salt_max)) +'-'+ str(int(max(Qi))) +'-'+ Pi[0] +'.csv'
    df.to_csv(filename)
    Li = Li.to_numpy()
    return Li,Ri,Qi,probability_distribution_list
def calcQueryCost(query_set,Qi):
    cost = 0
    for i in query_set:
        cost = cost + Qi[i]
    return cost
def testMinAlgorithm(Li,Ri,Qi,Pi):
    num_simulations = int(input('How many simulations would you like to test? '))
    min_index_list = []
    opt_query_list = []
    query_list = []
    heuristic_query_list = []
    for k in range(0,num_simulations):
        Vi = minimumProblemSimulation(Li,Ri,Pi)
        opt_minimal_index, opt_query_set = minimumProblemOptimalQuerySet(Li,Ri,Vi,Qi)
        query_set = approximationAlgorithm(Li,Ri,Qi,Pi,Vi)
        heuristic_query_set = heuristicOneApproximationAlgorithm(Li,Ri,Qi,Pi,Vi)
        min_index_list.append(opt_minimal_index)
        opt_query_list.append(opt_query_set)
        query_list.append(query_set)
        heuristic_query_list.append(heuristic_query_set)
    opt_costs = []
    algorithm_costs = []
    heuristic_costs = []
    comp_algorith = []
    comp_heuristic = []
    j = 0
    k = 0
    for i in opt_query_list:
        opt_costs.append(calcQueryCost(i,Qi))
        comp_algorith.append(calcQueryCost(query_list[j],Qi)/calcQueryCost(i,Qi))
        comp_heuristic.append(calcQueryCost(heuristic_query_list[k],Qi)/calcQueryCost(i,Qi))
        j =j+1
        k =k+1
    for j in query_list:
        algorithm_costs.append(calcQueryCost(j,Qi))
    for k in heuristic_query_list:
        heuristic_costs.append(calcQueryCost(k,Qi))
    expectedOpt = sum(opt_costs)/num_simulations
    expectedAlgo = sum(algorithm_costs)/num_simulations
    expectedHeuristicAlgo = sum(heuristic_costs)/num_simulations
    ratioAlgo = expectedAlgo/expectedOpt
    ratioHeuristicAlgo = expectedHeuristicAlgo/expectedOpt
    expectedCompAlgo = sum(comp_algorith)/num_simulations
    expectedCompHeuristic = sum(comp_heuristic)/num_simulations
    print('E[opt]: '+ str(expectedOpt))
    print('E[Alg]: ' + str(expectedAlgo))
    print('E[Heu]: ' + str(expectedHeuristicAlgo))
    print('comp ratio alg: ' + str(ratioAlgo))
    print('comp ratrio heu: ' + str(ratioHeuristicAlgo))
    print('E[alg/opt]: '+ str(expectedCompAlgo))
    print('E[heu/opt]: '+ str(expectedCompHeuristic))
    print(query_list)
    print(heuristic_query_list)
    '''min_index = pd.DataFrame(list(itertools.chain(*min_index_list)))
    #nu = min_index[0].value_counts()
    #ax = sns.barplot(x=nu.index,y=nu).set(title='Plot of the minimum index',xlabel='index', ylabel='Count')
    #ax.bar_label(ax.containers[0])
    #plt.show()
    #plt.savefig('MinimumIndex.png')
    optdata = pd.DataFrame(list(itertools.chain(*opt_query_list)))
    optvalue = optdata[0].value_counts()
    algodata = pd.DataFrame(list(itertools.chain(*query_list)))
    algovalue = algodata[0].value_counts()
    heuristicdata = pd.DataFrame(list(itertools.chain(*heuristic_query_list)))
    heuristicvalue = heuristicdata[0].value_counts()
    allValues = pd.DataFrame({'optimum':optvalue,'approx Algorithm':algovalue,'heuristic':heuristicvalue})
    print(allValues)
    df = pd.melt(allValues,id_vars=list(range(0,len(Li))), var_name="algorithm", value_name="count")
    print(df)
    bx = sns.catplot(x=list(range(0,len(Li))), y='count', hue='algorithm', data=df, kind='bar')
    plt.show()'''

Li = [0, 9.511885346386094, 9.60697009243154, 9.654185289779202, 9.730418461787217, 9.789282035843279, 9.885210832983462, 9.934999988303517, 9.971215924466557, 9.976376161303738]
Ri = [10, 19.511885346386094, 19.60697009243154, 19.6541852897792, 19.730418461787217, 19.78928203584328, 19.88521083298346, 19.934999988303517, 19.971215924466556, 19.97637616130374]
Qi = [50,5,5,2,1,2,2,1,1,5]
Pi = [1] * len(Li)
print('Instance 1 case 1.2')
testMinAlgorithm(Li,Ri,Qi,Pi)
Li = [0, 9.815421312880146, 9.843662412508552, 9.84528093866387, 9.905831711422326, 9.907239868130803, 9.941693807153053, 9.982184977950723, 9.982616317462947, 9.983592476481835]
Ri = [10, 19.815421312880147, 19.84366241250855, 19.84528093866387, 19.905831711422326, 19.9072398681308, 19.94169380715305, 19.982184977950723, 19.98261631746295, 19.983592476481835]
Qi = [45,28,1,1,6,2,1,3,1,1]
Pi = [1] * len(Li)
print('Instance 2 case 1.2')
testMinAlgorithm(Li,Ri,Qi,Pi)
Li = [0, 1, 9.60697009243154, 9.654185289779202, 9.730418461787217, 9.789282035843279, 9.885210832983462, 9.934999988303517, 9.971215924466557, 9.976376161303738]
Ri = [10, 19.511885346386094, 19.60697009243154, 19.6541852897792, 19.730418461787217, 19.78928203584328, 19.88521083298346, 19.934999988303517, 19.971215924466556, 19.97637616130374]
Qi = [70,60,5,2,1,2,2,1,1,5]
Pi = [1] * len(Li)
print('Instance 3 case 2.2')
testMinAlgorithm(Li,Ri,Qi,Pi)
Li = [0, 9, 9.842954342697427, 9.880345642368884, 9.898653507399464, 9.923405535777032, 9.926463823230803, 9.928932208838772, 9.976420388118637, 9.994833285992518]
Ri = [10, 12, 19.842954342697425, 19.880345642368884, 19.898653507399466, 19.923405535777032, 19.926463823230804, 19.928932208838773, 19.976420388118637, 19.99483328599252]
Qi = [35,24,1,1,1,1,1,1,1,1]
Pi = [1] * len(Li)
print('Instance 4 case 2.2')
testMinAlgorithm(Li,Ri,Qi,Pi)

def sortingProblem():
    print('lol')

def hypergraphOrientationProblem():
    print('h')
def test():
    p = 10 * ['1']
    m = minimumProblem(10,10,p,p)
    print(m)
    s = minimumProblemSimulation(m[0],m[1],m[3])
    print(s)
    q = minimumProblemOptimalQuerySet(m[0],m[1],s,p)
    print(q)
    print(len(q))
#test()
#start(0)