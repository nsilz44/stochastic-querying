This project is the experimental analysis of query-based algorithms.

# To Run the Results
type in python results.py

# Structure of the project
algortihms.py - contains the algorithms for the minimum problem.
hyperAlgorithm.py - contains the algorithms for the hypergraph orientation problem.
instanceGenerator.py - contains functions to generate instances for both the minimum problem and the hypergraph orientation problem.
main.py - contains functions to run the tests for the results. Important functions are testMinAlgorithm() and testHyperGraphAlgorithms() which are the sampling functions used in results.py.
optimalQuerySet.py - contains the optimal query algorithms for the minimum problem and the hypergraph orientation problem.
probabilities.py - contains the probability distributions for the project. 
results.py - contains the functions to run the experimental results as seen in the paper.
simulation.py - contains functions for running one simulation of an instance
visualisations.py - contains the visualisations of the results for the paper
\Figures - contains all the figures from visualisations.py
.csv - contain the results for each given test from results.py

# To add more probability distributions
create function to sample a point in a given range 
e.g def betaProb(l_endpoint,r_endpoint):
        a, b = 2, 0.8
        r = beta.rvs(a, b, size=1)
        return l_endpoint + r[0] * (r_endpoint-l_endpoint)
add the function to the function prob()
e.g elif probability_type == 2:
        r = betaProb(l_endpoint,r_endpoint)
create function to calculate the cdf of the distribution
e.g betaA, betaB = 2, 0.8
    betaRv = beta(betaA, betaB)
    def calcBetaProb(l_endpoint,r_endpoint,range):
        return(betaRv.cdf((r_endpoint - l_endpoint)/range))
add the function to the function calcProb()
e.g elif probability_type == 2:
        r = calcBetaProb(l_endpoint,r_endpoint,range)        
