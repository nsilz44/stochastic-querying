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
#testMinProbabilities()

def testMinIntervals():
    minDf = pd.DataFrame(columns=['Test', 'Number of intervals', 'Query structure', 'Probabilities',
       'Expected of optimum query set', 'Expected of approximation algorithm',
       'Expected of heuristic approximation algorithm',
       'Competitive ratio of approximation algorithm',
       'Competitive ratio of heuristic approximation algorithm',
       'Expected competitive ratio of approximation algorithm',
       'Expected competitive ratio of heuristic approximation algorithm',
       'Number of simulations'])
    Li = [0, 9, 9.842954342697427, 9.880345642368884, 9.898653507399464, 9.923405535777032, 9.926463823230803, 9.928932208838772, 9.976420388118637, 9.994833285992518]
    Ri = [10, 12, 19.842954342697425, 19.880345642368884, 19.898653507399466, 19.923405535777032, 19.926463823230804, 19.928932208838773, 19.976420388118637, 19.99483328599252]
    Qi = [60,30,4,1,6,2,1,3,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.2.1',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Li = [0, 9, 9.808777503284773, 9.831721725114067, 9.853301707684647, 9.853369739851248, 9.866552659061758, 9.905522824202134, 9.942362694502572, 9.95757069328152, 9.967860135910726, 9.969765139341945, 9.975372585037807, 9.97794358011316, 9.977982353979277, 9.986025539763457, 9.993985696355375, 9.995656353993654, 9.997651057879093, 9.998090009008589]
    Ri = [10, 12, 19.808777503284773, 19.831721725114065, 19.853301707684647, 19.853369739851246, 19.86655265906176, 19.905522824202134, 19.94236269450257, 19.957570693281518, 19.967860135910726, 19.969765139341945, 19.975372585037807, 19.977943580113163, 19.97798235397928, 19.986025539763457, 19.993985696355374, 19.995656353993652, 19.997651057879093, 19.99809000900859]
    Qi = [80,40,4,1,6,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.2.2',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Li = [0, 9, 9.8135693253059, 9.824888841677135, 9.833829794168917, 9.851209402119425, 9.867632306681367, 9.879801542491808, 9.890081989173783, 9.900789011628685, 9.914980512764654, 9.937968632547491, 9.942842015549878, 9.958126339656623, 9.977110355311968, 9.980123571603153, 9.986939205901374, 9.990054425465564, 9.995750689591695, 9.998392388395136, 9.99869409215628, 9.99897800847467, 9.999606663099579, 9.999695438234385, 9.999824453702443, 9.999888613440339, 9.999938737180283, 9.999942413588116, 9.999972136742175, 9.999989010819087]
    Ri = [10, 12, 19.8135693253059, 19.824888841677136, 19.833829794168917, 19.851209402119423, 19.867632306681365, 19.87980154249181, 19.890081989173783, 19.900789011628685, 19.914980512764654, 19.93796863254749, 19.94284201554988, 19.958126339656623, 19.977110355311968, 19.98012357160315, 19.986939205901372, 19.990054425465566, 19.995750689591695, 19.998392388395136, 19.998694092156278, 19.998978008474673, 19.999606663099577, 19.999695438234383, 19.999824453702445, 19.99988861344034, 19.999938737180283, 19.999942413588116, 19.999972136742173, 19.999989010819085]
    Qi = [100,50,1,1,6,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.2.3',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Li = [0, 9, 9.80332159657068, 9.810093368663386, 9.811333313258926, 9.831741817987766, 9.832493719195082, 9.84044209554069, 9.85668174516474, 9.872304178691069, 9.895638705169285, 9.900785383833421, 9.917896531155826, 9.92866731788071, 9.937380457073882, 9.939288730562748, 9.944684691092952, 9.954779365094073, 9.969455824185754, 9.97509330763902, 9.98662908534913, 9.993278818328683, 9.996090314231486, 9.997233424738491, 9.99823205597272, 9.998656447827038, 9.998792200920123, 9.99939449692243, 9.999461886579784, 9.999747688697887, 9.999928548709555, 9.999938611987742, 9.99998329513286, 9.999987469122845, 9.9999941924116, 9.99999769805259, 9.999998922812416, 9.999998966131306, 9.999999939703331, 9.999999963986129]
    Ri = [10, 12, 19.80332159657068, 19.810093368663388, 19.811333313258928, 19.831741817987766, 19.83249371919508, 19.840442095540688, 19.856681745164742, 19.872304178691067, 19.895638705169283, 19.900785383833423, 19.917896531155826, 19.92866731788071, 19.937380457073882, 19.939288730562748, 19.944684691092952, 19.954779365094073, 19.969455824185754, 19.97509330763902, 19.98662908534913, 19.993278818328683, 19.996090314231488, 19.99723342473849, 19.99823205597272, 19.998656447827038, 19.99879220092012, 19.99939449692243, 19.999461886579784, 19.999747688697887, 19.999928548709555, 19.999938611987744, 19.99998329513286, 19.999987469122843, 19.9999941924116, 19.99999769805259, 19.999998922812416, 19.999998966131308, 19.99999993970333, 19.999999963986127]
    Qi = [120,60,1,1,6,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.2.4',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    Li = [0, 9, 9.808051872689369, 9.814592770727014, 9.815593812952967, 9.829805998047133, 9.849593994840612, 9.85609682263782, 9.870711330609891, 9.89283122851827, 9.8952571215208, 9.91419771376241, 9.922892550480102, 9.928091521689392, 9.941443784595828, 9.949027027196589, 9.960311572646502, 9.961101549098062, 9.96207208672222, 9.9739931344179, 9.983018320953372, 9.984584193874365, 9.986313135399774, 9.988281583740838, 9.989188080540744, 9.992416847356884, 9.994248346815978, 9.99612242100069, 9.996451068648598, 9.997027123243962, 9.997407586623998, 9.998040457180144, 9.998615811294092, 9.999489306418173, 9.99957310245451, 9.999728048696696, 9.999838053666286, 9.999913903564847, 9.999967457335739, 9.99999078676368, 9.999995684613367, 9.999997265962522, 9.999998426548958, 9.999999325684767, 9.999999689015338, 9.9999998293436, 9.999999877618915, 9.99999995662579, 9.999999987074906, 9.99999998819365]
    Ri = [10, 12, 19.80805187268937, 19.814592770727014, 19.81559381295297, 19.829805998047135, 19.84959399484061, 19.85609682263782, 19.870711330609893, 19.89283122851827, 19.8952571215208, 19.914197713762412, 19.9228925504801, 19.928091521689392, 19.941443784595826, 19.94902702719659, 19.960311572646503, 19.96110154909806, 19.96207208672222, 19.9739931344179, 19.98301832095337, 19.984584193874365, 19.986313135399776, 19.988281583740836, 19.989188080540742, 19.992416847356886, 19.99424834681598, 19.996122421000692, 19.996451068648597, 19.99702712324396, 19.997407586624, 19.998040457180146, 19.998615811294094, 19.999489306418173, 19.999573102454512, 19.999728048696696, 19.999838053666288, 19.999913903564845, 19.99996745733574, 19.999990786763682, 19.999995684613367, 19.99999726596252, 19.999998426548956, 19.99999932568477, 19.99999968901534, 19.9999998293436, 19.999999877618915, 19.999999956625793, 19.999999987074908, 19.99999998819365]
    Qi = [140,70,1,1,6,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.2.5',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    print(minDf.head(6))
    minDf.to_csv('intervalsTests.csv')

#testMinIntervals()
def testSmallestElement():
    minDf = pd.DataFrame(columns=['Test', 'Number of intervals', 'Query structure', 'Probabilities',
       'Expected of optimum query set', 'Expected of approximation algorithm',
       'Expected of heuristic approximation algorithm',
       'Competitive ratio of approximation algorithm',
       'Competitive ratio of heuristic approximation algorithm',
       'Expected competitive ratio of approximation algorithm',
       'Expected competitive ratio of heuristic approximation algorithm',
       'Number of simulations'])
    Li = [0, 9.511885346386094, 9.60697009243154, 9.654185289779202, 9.730418461787217, 9.789282035843279, 9.885210832983462, 9.934999988303517, 9.971215924466557, 9.976376161303738]
    Ri = [10, 19.511885346386094, 19.60697009243154, 19.6541852897792, 19.730418461787217, 19.78928203584328, 19.88521083298346, 19.934999988303517, 19.971215924466556, 19.97637616130374]
    Qi = [50,5,5,2,1,2,2,1,1,5]
    Pi = [1] * len(Li)
    print('Instance 1 case 1.1')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.1',len(Li),'All uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
   
    Li = [0, 9.511885346386094, 9.60697009243154, 9.654185289779202, 9.730418461787217, 9.789282035843279, 9.885210832983462, 9.934999988303517, 9.971215924466557, 9.976376161303738]
    Ri = [10, 19.511885346386094, 19.60697009243154, 19.6541852897792, 19.730418461787217, 19.78928203584328, 19.88521083298346, 19.934999988303517, 19.971215924466556, 19.97637616130374]
    Qi = [1] * len(Li)
    Pi = [1] * len(Li)
    print('Instance 1 case 1.2')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.2',len(Li),'Descending high to low then random low','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    Li = [0, 9.815421312880146, 9.843662412508552, 9.84528093866387, 9.905831711422326, 9.907239868130803, 9.941693807153053, 9.982184977950723, 9.982616317462947, 9.983592476481835]
    Ri = [10, 19.815421312880147, 19.84366241250855, 19.84528093866387, 19.905831711422326, 19.9072398681308, 19.94169380715305, 19.982184977950723, 19.98261631746295, 19.983592476481835]
    Qi = [1] * len(Li)
    Pi = [1] * len(Li)
    print('Instance 2 case 1.1')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.3',len(Li),'All uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    Li = [0, 9.815421312880146, 9.843662412508552, 9.84528093866387, 9.905831711422326, 9.907239868130803, 9.941693807153053, 9.982184977950723, 9.982616317462947, 9.983592476481835]
    Ri = [10, 19.815421312880147, 19.84366241250855, 19.84528093866387, 19.905831711422326, 19.9072398681308, 19.94169380715305, 19.982184977950723, 19.98261631746295, 19.983592476481835]
    Qi = [45,28,1,1,6,2,1,3,1,1]
    Pi = [1] * len(Li)
    print('Instance 2 case 1.2')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.4',len(Li),'Descending high to low then random low','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    Li = [0, 1, 9.60697009243154, 9.654185289779202, 9.730418461787217, 9.789282035843279, 9.885210832983462, 9.934999988303517, 9.971215924466557, 9.976376161303738]
    Ri = [10, 19.511885346386094, 19.60697009243154, 19.6541852897792, 19.730418461787217, 19.78928203584328, 19.88521083298346, 19.934999988303517, 19.971215924466556, 19.97637616130374]
    Qi = [1] * len(Li)
    Pi = [1] * len(Li)
    print('Instance 3 case 2.1')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.5',len(Li),'All uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    Li = [0, 1, 9.60697009243154, 9.654185289779202, 9.730418461787217, 9.789282035843279, 9.885210832983462, 9.934999988303517, 9.971215924466557, 9.976376161303738]
    Ri = [10, 19.511885346386094, 19.60697009243154, 19.6541852897792, 19.730418461787217, 19.78928203584328, 19.88521083298346, 19.934999988303517, 19.971215924466556, 19.97637616130374]
    Qi = [70,60,5,2,1,2,2,1,1,5]
    Pi = [1] * len(Li)
    print('Instance 3 case 2.2')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.6',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    Li = [0, 9, 9.842954342697427, 9.880345642368884, 9.898653507399464, 9.923405535777032, 9.926463823230803, 9.928932208838772, 9.976420388118637, 9.994833285992518]
    Ri = [10, 12, 19.842954342697425, 19.880345642368884, 19.898653507399466, 19.923405535777032, 19.926463823230804, 19.928932208838773, 19.976420388118637, 19.99483328599252]
    Qi = [1] * len(Li)
    Pi = [1] * len(Li)
    print('Instance 4 case 2.1')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.7',len(Li),'All uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    Li = [0, 9, 9.842954342697427, 9.880345642368884, 9.898653507399464, 9.923405535777032, 9.926463823230803, 9.928932208838772, 9.976420388118637, 9.994833285992518]
    Ri = [10, 12, 19.842954342697425, 19.880345642368884, 19.898653507399466, 19.923405535777032, 19.926463823230804, 19.928932208838773, 19.976420388118637, 19.99483328599252]
    Qi = [35,24,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    print('Instance 4 case 2.2')
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.3.8',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    
    print(minDf.head(8))
    minDf.to_csv('uniformityTests.csv')

#testSmallestElement()

def testHypergraphProbabilities():
    hyperDf = pd.DataFrame(columns=['Test', 'Number of intervals', 'Number of edges', 'Graph','Edges Structure', 'Query structure', 'Probabilities',
       'Expected of optimum query set', 'Expected of threshold algorithm',
       'Expected of bestVc algorithm',
       'Competitive ratio of threshold algorithm',
       'Competitive ratio of bestVc algorithm',
       'Expected competitive ratio of threshold algorithm',
       'Expected competitive ratio of bestVc algorithm',
       'Number of simulations'])
    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [1]* len(Li)
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.1',len(Li),len(Ei),'HyperGraph','Random between 2 and 4 in length','uniform','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [2]* len(Li)
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.2',len(Li),len(Ei),'HyperGraph','Random between 2 and 4 in length','uniform','All beta',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [3]* len(Li)
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.3',len(Li),len(Ei),'HyperGraph','Random between 2 and 4 in length','uniform','All semi-circular',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [4]* len(Li)
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.4',len(Li),len(Ei),'HyperGraph','Random between 2 and 4 in length','uniform','All gauss-hyper',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [5]* len(Li)
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.5',len(Li),len(Ei),'HyperGraph','Random between 2 and 4 in length','uniform','All rdist',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.44086262555211, 6.508807617982692, 15.289007942473924, 25.033473676661764, 33.64226148658999, 38.850973234120346, 42.90820582788927, 44.088051844840344, 53.40918622238459, 61.12098058859728, 64.6371169529308, 74.23323384528064, 75.7017748732943, 77.83736136953749, 79.72367983795047]
    Ri = [80.38122255704386, 81.86113242068102, 82.37233754314828, 86.11998369082504, 86.53574994809362, 89.54584401255563, 92.01545658320191, 98.45394662476168, 100.01817799769347, 104.12260944552939, 104.3200027903787, 105.59635129807364, 112.30390648855867, 112.63978902141035, 119.27054081198723]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [6]* len(Li)
    Ei = [[4, 6, 11], [0, 10, 12, 13], [1, 4, 7, 14], [8, 11], [8, 12], [1, 3, 7], [2, 6, 8, 11], [0, 13], [1, 2, 9], [0, 5, 6, 13]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.6',len(Li),len(Ei),'HyperGraph','Random between 2 and 4 in length','uniform','All bradford',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [1] * len(Li)
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.7',len(Li),len(Ei),'Bipatite Graph','2 in length','uniform','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [2] * len(Li)
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.8',len(Li),len(Ei),'Bipatite Graph','2 in length','uniform','All beta',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [3] * len(Li)
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.9',len(Li),len(Ei),'Bipatite Graph','2 in length','uniform','All semi-circular',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [4] * len(Li)
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.10',len(Li),len(Ei),'Bipatite Graph','2 in length','uniform','All gauss-hyper',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [5] * len(Li)
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.11',len(Li),len(Ei),'Bipatite Graph','2 in length','uniform','All r-dist',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    Li = [5.07250462062994, 13.532797387649257, 16.597993985971456, 24.270996359293463, 25.378232465475932, 32.755363787401535, 38.10592029009122, 47.1222594336827, 55.16083802965181, 58.216503100273044]
    Ri = [61.12150622392756, 67.1445669193577, 71.07159554132309, 75.38154846662785, 82.41765493672142, 89.40367464611927, 96.36691453057935, 97.1736713649101, 103.93669146225206, 108.07853563383954]
    Qi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Pi = [6] * len(Li)
    Ei = [[0, 5], [0, 8], [1, 6], [1, 7], [1, 8], [1, 9], [2, 6], [2, 8], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 9]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.1.12',len(Li),len(Ei),'Bipatite Graph','2 in length','uniform','All bradford',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)

    hyperDf.to_csv('hyperProbabilityTests.csv')
#testHypergraphProbabilities()

def testHyperGraphs():
    hyperDf = pd.DataFrame(columns=['Test', 'Number of intervals', 'Number of edges', 'Graph','Edges Structure', 'Query structure', 'Probabilities',
       'Expected of optimum query set', 'Expected of threshold algorithm',
       'Expected of bestVc algorithm',
       'Competitive ratio of threshold algorithm',
       'Competitive ratio of bestVc algorithm',
       'Expected competitive ratio of threshold algorithm',
       'Expected competitive ratio of bestVc algorithm',
       'Number of simulations'])
    Li = [19.77941279190243, 23.84073999216108, 31.347167746178364, 43.448155584673785, 49.18570896485677, 58.87887262505179, 69.41793558927026, 76.1356040082379, 82.09511967781414, 97.0162221055431, 107.97626951742812, 120.76756848348839, 138.10890651558068, 154.76621347715874, 161.77685790780689, 172.49522381082957, 179.52157980787914, 187.300424885976, 191.21516367748907, 208.7286992797203]
    Ri = [212.88075054619856, 224.094339735388, 238.05635179538564, 249.10430352823627, 251.7811332551438, 268.8315617928097, 274.80520320161327, 291.35163682230484, 308.16602134086537, 312.63249573689774, 325.03743942860746, 341.43289157578863, 343.34129507483254, 345.33623803462933, 358.64606085152997, 359.188457722872, 376.36496230610715, 388.897060413993, 391.8285211059368, 399.0398621173606]
    Qi = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Pi = [1]*len(Li)
    Ei = [[0, 16], [0, 17], [0, 18], [0, 19], [1, 12], [1, 13], [1, 15], [1, 17], [2, 12], [2, 13], [2, 15], [2, 18], [2, 19], [3, 15], [3, 16], [3, 17], [3, 18], [3, 19], [4, 10], [4, 11], [4, 13], [4, 14], [4, 15], [4, 17], [5, 10], [5, 11], [5, 12], [5, 14], [5, 15], [5, 16], [5, 19], [6, 10], [6, 11], [6, 14], [6, 17], [6, 18], [7, 14], [7, 15], [7, 16], [7, 18], [8, 11], [8, 15], [9, 11], [9, 12], [9, 13], [9, 16], [9, 17]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.2.1',len(Li),len(Ei),'Bipatite Graph','2 in length','descending','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)
    
    Ei =[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.2.2',len(Li),len(Ei),'Path Graph','2 in length','descending','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)
    
    Ei = [[6, 12], [6, 7], [6, 13], [12, 15], [0, 12], [3, 10], [3, 9], [3, 17], [10, 15], [1, 10], [0, 2], [0, 7], [2, 5], [2, 18], [8, 9], [8, 18], [8, 19], [9, 14], [5, 16], [5, 17], [13, 16], [4, 16], [4, 14], [1, 14], [17, 18], [15, 19], [7, 13], [4, 11], [1, 11], [11, 19]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.2.3',len(Li),len(Ei),'Random 3 degree Graph','2 in length','descending','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)
    
    Ei = [[8, 12], [8, 10], [12, 14], [9, 17], [9, 18], [13, 17], [2, 5], [2, 4], [5, 14], [1, 3], [1, 4], [3, 18], [10, 13], [16, 19], [11, 16], [15, 19], [0, 7], [0, 6], [6, 7], [11, 15]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.2.4',len(Li),len(Ei),'Random 2 degree Graph','2 in length','descending','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)
    
    Ei = [[0, 12], [0, 16], [1, 3], [1, 19], [1, 13], [2, 9], [2, 4], [2, 13], [2, 11], [2, 15], [3, 6], [4, 12], [5, 18], [6, 8], [7, 10], [8, 12], [9, 17], [10, 14], [11, 18], [18, 19]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.2.5',len(Li),len(Ei),'Random GNM 20 edges Graph','2 in length','descending','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)
    
    Ei = [[0, 14], [0, 12], [0, 8], [1, 10], [1, 17], [2, 17], [3, 16], [4, 16], [4, 13], [4, 8], [5, 18], [5, 9], [6, 19], [6, 18], [7, 13], [7, 10], [7, 18], [8, 14], [10, 11], [10, 16], [10, 12], [10, 14], [11, 15], [11, 12], [12, 15], [12, 14], [12, 17], [13, 16], [14, 18], [17, 18]]
    expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations = testHyperGraphAlgorithms(Li,Ri,Qi,Pi,Ei)
    hyperDf = pd.concat([pd.DataFrame([['2.2.6',len(Li),len(Ei),'Random GNM 30 edges Graph','2 in length','descending','All uniform',expectedOpt, expectedThreshold, expectedBestVC, ratioThreshold, ratioBestVc, expectedCompThreshold, expectedCompBestVc, num_simulations]], columns=hyperDf.columns), hyperDf], ignore_index=True)
    
    hyperDf.to_csv('GraphTests.csv')

testHyperGraphs()

