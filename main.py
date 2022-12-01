from probabilities import *
from instanceGenerator import *
from simulation import *
from optimalQuerySet import *
import pandas as pd


def start(a):
    if a == 1:
        print('Not a problem')
    print('Type in the problem you would like to test')
    print('Type "m" for the smallest element problem')
    print('Type "s" for the sorting problem')
    print('Type "h" for the hypergraph orientation problem')
    problem = input('')
    if problem == 'm':
        makeMinimumProblem(0)
    elif problem == 's':
        sortingProblem()
    elif problem == 'h':
        hypergraphOrientationProblem()
    else:
        start(1)

def makeMinimumProblem(a):
    if a == 1:
        print('Try again')
    print('Type "i" to import an instance')
    print('Type "n" to create a new instance')
    instance = input('')
    if instance == 'i':
        print('Type in the csv file with the previous instance')
        csvFile = input('')
        df = pd.read_csv(csvFile)
    elif instance == 'n':
        #(num_of_intervals,salt_max,Qi,probability_distribution_list)
        Li,Ri,Qi,probability_distribution_list = createInstanceMinimumProblem()
    else:
        minimumProblem(1)

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
    Li,Ri,Qi,probability_distribution_list = minimumProblem(num_of_intervals,salt_max,Qi,probability_distribution_list)
    print(Ri)
    return Li,Ri,Qi,probability_distribution_list

    
def sortingProblem():
    print('lol')

def hypergraphOrientationProblem():
    print('h')
def test():
    p = 10 * ['1']
    m = minimumProblem(10,10,1,0,p)
    print(m)
    s = minimumProblemSimulation(m[0],m[1],m[3])
    print(s)
    q = minimumProblemUniformOptimalQuerySet(m[0],m[1],s)
    print(q)
    print(len(q))
#test()
start(0)