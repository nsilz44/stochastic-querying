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

def minimumProblem():
    print('here')

def sortingProblem():
    print('lol')

def hypergraphOrientationProblem():
    print('h')
def test():
    p = 10 * ['1']
    m = minimum_problem(10,10,1,0,p)
    print(m)
    s = minimumProblemSimulation(m[0],m[1],m[3])
    print(s)
    q = minimumProblemUniformOptimalQuerySet(m[0],m[1],s)
    print(q)
    print(len(q))
#test()
start(0)