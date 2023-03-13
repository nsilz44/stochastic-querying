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
    Li = [0, 9.801327781222579, 9.808051872689369, 9.814592770727014, 9.815593812952967, 9.829805998047133, 9.849593994840612, 9.85609682263782, 9.870711330609891, 9.89283122851827, 9.8952571215208, 9.91419771376241, 9.922892550480102, 9.928091521689392, 9.941443784595828, 9.949027027196589, 9.960311572646502, 9.961101549098062, 9.96207208672222, 9.9739931344179, 9.983018320953372, 9.984584193874365, 9.986313135399774, 9.988281583740838, 9.989188080540744, 9.992416847356884, 9.994248346815978, 9.99612242100069, 9.996451068648598, 9.997027123243962, 9.997407586623998, 9.998040457180144, 9.998615811294092, 9.999489306418173, 9.99957310245451, 9.999728048696696, 9.999838053666286, 9.999913903564847, 9.999967457335739, 9.99999078676368, 9.999995684613367, 9.999997265962522, 9.999998426548958, 9.999999325684767, 9.999999689015338, 9.9999998293436, 9.999999877618915, 9.99999995662579, 9.999999987074906, 9.99999998819365]
    Ri = [10, 19.80132778122258, 19.80805187268937, 19.814592770727014, 19.81559381295297, 19.829805998047135, 19.84959399484061, 19.85609682263782, 19.870711330609893, 19.89283122851827, 19.8952571215208, 19.914197713762412, 19.9228925504801, 19.928091521689392, 19.941443784595826, 19.94902702719659, 19.960311572646503, 19.96110154909806, 19.96207208672222, 19.9739931344179, 19.98301832095337, 19.984584193874365, 19.986313135399776, 19.988281583740836, 19.989188080540742, 19.992416847356886, 19.99424834681598, 19.996122421000692, 19.996451068648597, 19.99702712324396, 19.997407586624, 19.998040457180146, 19.998615811294094, 19.999489306418173, 19.999573102454512, 19.999728048696696, 19.999838053666288, 19.999913903564845, 19.99996745733574, 19.999990786763682, 19.999995684613367, 19.99999726596252, 19.999998426548956, 19.99999932568477, 19.99999968901534, 19.9999998293436, 19.999999877618915, 19.999999956625793, 19.999999987074908, 19.99999998819365]
    Qi = [140,70,1,1,6,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    Pi = [1] * len(Li)
    expectedOpt, expectedAlgo, expectedHeuristicAlgo, ratioAlgo, ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations = testMinAlgorithm(Li,Ri,Qi,Pi)
    minDf = pd.concat([pd.DataFrame([['1.2.5',len(Li),'Descending high to low to uniform','All uniform',expectedOpt,expectedAlgo,expectedHeuristicAlgo,ratioAlgo,ratioHeuristicAlgo,expectedCompAlgo, expectedCompHeuristic, num_simulations]], columns=minDf.columns), minDf], ignore_index=True)
    print(minDf.head(6))
    minDf.to_csv('intervalsTests.csv')

testMinIntervals()