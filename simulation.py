from probabilities import *
from instanceGenerator import *

def minimumProblemSimulation(Li,Ri,Pi):
    n = len(Li)
    Vi = []
    for i in range(0,n):
        value = prob(Pi[i],Li[i],Ri[i])
        Vi.append(value)
    return (Vi)

'''p= 10 * ['1']
m = minimumProblem(10,10,1,0,p)
print(m)
print(minimumProblemSimulation(m[0],m[1],m[3]))'''