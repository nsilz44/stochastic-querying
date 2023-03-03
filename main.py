from probabilities import *
from instanceGenerator import *
from simulation import *
from optimalQuerySet import *
from algortihms import *
from hyperAlgorithm import *
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
    #print(query_list)
    #print(heuristic_query_list)
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


def test_smallest_element():
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
    Li = [0, 9, 9.842954342697427, 9.880345642368884, 9.898653507399464, 9.923405535777032, 9.926463823230803, 9.928932208838772, 9.976420388118637, 9.994833285992518]
    Ri = [10, 12, 19.842954342697425, 19.880345642368884, 19.898653507399466, 19.923405535777032, 19.926463823230804, 19.928932208838773, 19.976420388118637, 19.99483328599252]
    Qi = [1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    print('Instance 5')
    testMinAlgorithm(Li,Ri,Qi,Pi)
    Li = [0, 9.804981484093497, 9.808777503284773, 9.831721725114067, 9.853301707684647, 9.853369739851248, 9.866552659061758, 9.905522824202134, 9.942362694502572, 9.95757069328152, 9.967860135910726, 9.969765139341945, 9.975372585037807, 9.97794358011316, 9.977982353979277, 9.986025539763457, 9.993985696355375, 9.995656353993654, 9.997651057879093, 9.998090009008589]
    Ri = [10, 19.804981484093496, 19.808777503284773, 19.831721725114065, 19.853301707684647, 19.853369739851246, 19.86655265906176, 19.905522824202134, 19.94236269450257, 19.957570693281518, 19.967860135910726, 19.969765139341945, 19.975372585037807, 19.977943580113163, 19.97798235397928, 19.986025539763457, 19.993985696355374, 19.995656353993652, 19.997651057879093, 19.99809000900859]
    Qi = [100,28,1,1,6,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    print('Instance 6 ')
    testMinAlgorithm(Li,Ri,Qi,Pi)


def testBipartiteInstances():
    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    Li = [19.77941279190243, 23.84073999216108, 31.347167746178364, 43.448155584673785, 49.18570896485677, 58.87887262505179, 69.41793558927026, 76.1356040082379, 82.09511967781414, 97.0162221055431, 107.97626951742812, 120.76756848348839, 138.10890651558068, 154.76621347715874, 161.77685790780689, 172.49522381082957, 179.52157980787914, 187.300424885976, 191.21516367748907, 208.7286992797203]
    Ri = [212.88075054619856, 224.094339735388, 238.05635179538564, 249.10430352823627, 251.7811332551438, 268.8315617928097, 274.80520320161327, 291.35163682230484, 308.16602134086537, 312.63249573689774, 325.03743942860746, 341.43289157578863, 343.34129507483254, 345.33623803462933, 358.64606085152997, 359.188457722872, 376.36496230610715, 388.897060413993, 391.8285211059368, 399.0398621173606]
    Qi = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Pi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Ei = [[0, 16], [0, 17], [0, 18], [0, 19], [1, 12], [1, 13], [1, 15], [1, 17], [2, 12], [2, 13], [2, 15], [2, 18], [2, 19], [3, 15], [3, 16], [3, 17], [3, 18], [3, 19], [4, 10], [4, 11], [4, 13], [4, 14], [4, 15], [4, 17], [5, 10], [5, 11], [5, 12], [5, 14], [5, 15], [5, 16], [5, 19], [6, 10], [6, 11], [6, 14], [6, 17], [6, 18], [7, 14], [7, 15], [7, 16], [7, 18], [8, 11], [8, 15], [9, 11], [9, 12], [9, 13], [9, 16], [9, 17]]
    testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)

def testPathInstance():
    Li = [9.588138332999435, 10.328769267185857, 17.97266737973637, 27.63709787310679, 29.87578948462938, 30.93188822311162, 31.42592843900378, 33.49286526164367, 39.26193010666598, 48.823148403598026, 53.60864068916762, 55.33934238083748, 58.86688212686037, 67.68139013533336, 70.8365395355455, 75.95144817169562, 76.87142874952164, 79.57639799000361, 89.14846968209103, 99.0068031746348]
    Ri = [107.07408678926379, 113.90200293932044, 115.70799725560553, 117.72849276418279, 119.03814208736317, 121.21637129570901, 130.09281760910204, 137.6396681920132, 140.07850353839916, 147.58156785786502, 156.85445262002114, 158.56568402035364, 166.42904647046225, 166.86133317159843, 169.83521216743793, 173.97336603173372, 175.2585766399794, 178.03477348389336, 187.96397793929506, 197.05570033072533]
    Qi = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Pi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Ei = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19],[0,19]]
    testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)

def testHyperGraphs():
    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 6, 13]]
    testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    Li = [9.340971873588874, 13.85204527081042, 22.024485898153088, 27.46203412811856, 35.018981769822446, 44.13933530455427, 45.90567243793295, 52.70718748552208, 57.45178485429612, 60.50562599395085, 66.57402534443152, 71.54619977053582, 76.03333299514014, 81.36560704997241, 85.59755355757856, 88.53018038347633, 91.64720567889647, 93.13887768427645, 94.77018319603796, 99.31790916593715]
    Ri = [100.34568668346444, 108.90388887507899, 110.08507724154227, 118.01113313160317, 121.15692334797122, 128.2386123964225, 132.1871777882473, 132.44886643962556, 132.65546670834334, 142.34581650737766, 145.67928962861382, 154.66583895093382, 160.95795362700895, 170.21055964516157, 176.21954637898898, 178.37813525462474, 185.18502986030208, 191.51480022402362, 197.94755186290348, 201.1305084389329]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Ei = [[11, 15], [1, 3, 5, 9, 18], [5, 8], [9, 13, 15], [0, 9, 18], [0, 13, 14, 15, 19], [1, 13, 17], [2, 9, 15, 17], [0, 5, 19], [1, 8, 11, 16], [0, 5, 8, 15], [4, 16, 18], [2, 3, 4, 9, 19], [0, 17, 18], [2, 15, 19]]
    testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
def testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei):
    num_simulations = int(input('How many simulations would you like to test? '))
    opt_query_list = []
    threshold_query_list = []
    bestvc_query_list = []
    Mi = findMandatoryProbabilities(Li,Ri,Qi,Pi,Ei,10000)
    d = 2 / (1 + math.sqrt(5))
    for k in range(0,num_simulations):
        Vi = minimumProblemSimulation(Li,Ri,Pi)
        opt_query_set = hypergraphOptimalQuerySet(Li,Ri,Vi,Qi,Ei)
        query_set = thresholdLIPAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi)
        bestvc_query_set = bestVCAlgorithm(Li,Ri,Qi,Pi,Mi,Ei,Vi)
        opt_query_list.append(opt_query_set)
        threshold_query_list.append(query_set)
        bestvc_query_list.append(bestvc_query_set)
    opt_costs = []
    threshold_costs = []
    bestvc_costs = []
    comp_threshold = []
    comp_bestvc = []
    j = 0
    k = 0
    for i in opt_query_list:
        opt_costs.append(calcQueryCost(i,Qi))
        comp_threshold.append(calcQueryCost(threshold_query_list[j],Qi)/calcQueryCost(i,Qi))
        comp_bestvc.append(calcQueryCost(bestvc_query_list[k],Qi)/calcQueryCost(i,Qi))
        j =j+1
        k =k+1
    for j in threshold_query_list:
        threshold_costs.append(calcQueryCost(j,Qi))
    for k in bestvc_query_list:
        bestvc_costs.append(calcQueryCost(k,Qi))
    expectedOpt = sum(opt_costs)/num_simulations
    expectedThreshold = sum(threshold_costs)/num_simulations
    expectedHeuristicAlgo = sum(bestvc_costs)/num_simulations
    ratioAlgo = expectedThreshold/expectedOpt
    ratioHeuristicAlgo = expectedHeuristicAlgo/expectedOpt
    expectedCompAlgo = sum(comp_threshold)/num_simulations
    expectedCompHeuristic = sum(comp_bestvc)/num_simulations
    print('E[opt]: '+ str(expectedOpt))
    print('E[Thr]: ' + str(expectedThreshold))
    print('E[BestVc]: ' + str(expectedHeuristicAlgo))
    print('comp ratio Thr: ' + str(ratioAlgo))
    print('comp ratrio BestVc: ' + str(ratioHeuristicAlgo))
    print('E[Thr/opt]: '+ str(expectedCompAlgo))
    print('E[BestVc/opt]: '+ str(expectedCompHeuristic))

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

#testBipartiteInstances()
#testPathInstance()
testHyperGraphs()