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


Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Pi = [6]* len(Li)
Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
Mi = findMandatoryProbabilities(Li,Ri,Qi,Pi,Ei,1000)
d = 2 / (1 + math.sqrt(5))
c = input('')
while c != 'a':
    print('Li:',Li)
    print('Ri:',Ri)
    print('Qi:',Qi)
    print('Pi:',Pi,'All the bradford distribution')
    print('Ei:',Ei)
    Vi = minimumProblemSimulation(Li,Ri,Pi)
    print('Vi:',Vi)
    opt = hypergraphOptimalQuerySet(Li,Ri,Vi,Qi,Ei)
    thr = thresholdLIPAlgorithm(Li,Ri,Qi,Pi,Mi,d,Ei,Vi)
    bstvc = bestVCAlgorithm(Li,Ri,Qi,Pi,Mi,Ei,Vi)
    print('Threshold query set:',thr,'with query cost:',calcQueryCost(thr,Qi))
    print('BestVc query set',bstvc,'with query cost:',calcQueryCost(bstvc,Qi))
    print('Optimal query set',opt,'with query cost:',calcQueryCost(opt,Qi))
    c = input('')
    