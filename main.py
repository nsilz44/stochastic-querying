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
        minimumProblem()
    elif problem == 's':
        sortingProblem()
    elif problem == 'h':
        hypergraphOrientationProblem()
    else:
        start(1)

def minimumProblem(a):
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
        #(num_of_intervals,salt_max,query_cost_uniformness,query_cost_max,probability_distribution_list)
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