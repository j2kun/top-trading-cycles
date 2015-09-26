import random

# serialDictatorship: [[int]], [int] -> {int: int}
# construct a pareto-optimal allocation of objects to agents.
def serialDictatorship(agents, objects, seed=None):
   if seed is not None:
      random.seed(seed)

   agentPreferences = agents[:]
   random.shuffle(agentPreferences)
   allocation = dict()
   availableHouses = set(objects[:])

   for agentIndex, preference in enumerate(agentPreferences):
      allocation[agentIndex] = max(availableHouses, key=preference.index)
      availableHouses.remove(allocation[agentIndex])

   return allocation


if __name__ == "__main__":
   from unittest import test

   agents = [['a','b','c','d'], ['a','b','c','d'], ['a','b','c','d'], ['a','b','c','d']]
   objects = ['a','b','c','d']
   allocation = serialDictatorship(agents, objects, seed=1)
   test({0: 'd', 1: 'c', 2: 'b', 3: 'a'}, allocation)


   agents = [['d','a','c','b'], # 4th
             ['a','d','c','b'], # 3rd
             ['a','d','b','c'], # 2nd
             ['d','a','c','b']] # 1st
   objects = ['a','b','c','d']
   allocation = serialDictatorship(agents, objects, seed=1)
   test({0: 'b', 1: 'c', 2: 'd', 3: 'a'}, allocation)
