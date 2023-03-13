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
from main import *



def testMinProbabilities():
    minDf = pd.DataFrame(columns=['Test', 'Number of intervals', 'Query structure', 'Probabilities',
       'Expected of optimum query set', 'Expected of approximation algorithm',
       'Expected of heuristic approximation algorithm',
       'Competitive ratio of approximation algorithm',
       'Competitive ratio of heuristic approximation algorithm',
       'Expected competitive ratio of approximation algorithm',
       'Expected competitive ratio of heuristic approximation algorithm',
       'Number of simulations'])
    Li = [0, 9, 9.808777503284773, 9.831721725114067, 9.853301707684647, 9.853369739851248, 9.866552659061758, 9.905522824202134, 9.942362694502572, 9.95757069328152, 9.967860135910726, 9.969765139341945, 9.975372585037807, 9.97794358011316, 9.977982353979277]
    Ri = [10, 19.804981484093496, 19.808777503284773, 19.831721725114065, 19.853301707684647, 19.853369739851246, 19.86655265906176, 19.905522824202134, 19.94236269450257, 19.957570693281518, 19.967860135910726, 19.969765139341945, 19.975372585037807, 19.977943580113163, 19.97798235397928]
    Qi = [50,15,5,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.1.1',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Pi = [2] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.1.2',len(Li),'Descending high to low to uniform','All beta distribution',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Pi = [3] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.1.3',len(Li),'Descending high to low to uniform','All semi-circular distribution',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Pi = [4] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.1.4',len(Li),'Descending high to low to uniform','All Gauss hyper distribution',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Pi = [5] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.1.5',len(Li),'Descending high to low to uniform','All r-distribution',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Pi = [6] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.1.6',len(Li),'Descending high to low to uniform','All bradford distribution',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    print(minDf.head(6))
    minDf.to_csv('probabilityTests.csv')
testMinProbabilities()