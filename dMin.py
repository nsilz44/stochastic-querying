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

while c != 'a':
    Li = [0, 9, 9.808777503284773, 9.831721725114067, 9.853301707684647, 9.853369739851248, 9.866552659061758, 9.905522824202134, 9.942362694502572, 9.95757069328152, 9.967860135910726, 9.969765139341945, 9.975372585037807, 9.97794358011316, 9.977982353979277]
    Ri = [10, 19.804981484093496, 19.808777503284773, 19.831721725114065, 19.853301707684647, 19.853369739851246, 19.86655265906176, 19.905522824202134, 19.94236269450257, 19.957570693281518, 19.967860135910726, 19.969765139341945, 19.975372585037807, 19.977943580113163, 19.97798235397928]
    Qi = [50,15,5,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [6] * len(Li)
    print('Li:',Li)
    print('Ri:',Ri)
    print('Qi:',Qi)
    print('Pi:',Pi,'All the bradford distribution')
    Vi = minimumProblemSimulation(Li,Ri,Pi)
    print('Vi:',Vi)
    opt_minimal_index,opt = minimumProblemOptimalQuerySet(Li,Ri,Vi,Qi)
    alg = approximationAlgorithm(Li,Ri,Qi,Pi,Vi)
    heu = heuristicOneApproximationAlgorithm(Li,Ri,Qi,Pi,Vi)
    print('Approximation query set:',alg,'with query cost:',calcQueryCost(alg,Qi))
    print('Heuristic query set',heu,'with query cost:',calcQueryCost(heu,Qi))
    print('Optimal query set',opt,'with query cost:',calcQueryCost(opt,Qi))
    c = input('')