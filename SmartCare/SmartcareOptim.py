

##First approach
##https://sandipanweb.wordpress.com/2020/12/08/travelling-salesman-problem-tsp-with-python/
import mlrose
import numpy as np


# Create list of city coordinates
coords_list = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]

# Initialize fitness function object using coords_list
fitness_coords = mlrose.TravellingSales(coords = coords_list)

# Create list of distances between pairs of cities
dist_list = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426), \
             (0, 5, 5.3852), (0, 6, 4.0000), (0, 7, 2.2361), (1, 2, 1.0000), \
             (1, 3, 2.8284), (1, 4, 2.0000), (1, 5, 4.1231), (1, 6, 4.2426), \
             (1, 7, 2.2361), (2, 3, 2.2361), (2, 4, 2.2361), (2, 5, 4.4721), \
             (2, 6, 5.0000), (2, 7, 3.1623), (3, 4, 2.0000), (3, 5, 3.6056), \
             (3, 6, 5.0990), (3, 7, 4.1231), (4, 5, 2.2361), (4, 6, 3.1623), \
             (4, 7, 2.2361), (5, 6, 2.2361), (5, 7, 3.1623), (6, 7, 2.2361)]

# Initialize fitness function object using dist_list
fitness_dists = mlrose.TravellingSales(distances = dist_list)


problem_fit = mlrose.TSPOpt(length = 8, fitness_fn = fitness_coords,
                            maximize=False)

coords_list = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6),
               (1, 5), (2, 3)]
problem_no_fit = mlrose.TSPOpt(length = 8, coords = coords_list,
                               maximize=False)


# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)

print('The best state found is: ', best_state)

print('The fitness at the best state is: ', best_fitness)



# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
					      max_attempts = 100, random_state = 2)

print('The best state found is: ', best_state)



##Second approach that relies on classes and OOP
#import dependencies
import numpy as np
import random
import matplotlib.pyplot as plt
#helper function that deletes all values from a that are also in b
def deletebfroma(a,b):
    index = np.array([], dtype = np.int16)
    for number in range(len(a)):
        if a[number] in b:
            index = np.append(index, number)

    return np.delete(a, index)

    # the whole thing is an object
class salesman(object):
    #initialize the object
    def __init__(self, xymax, numberofstops, maxmen, mutationrate, verbose = False, mutatebest = True):

        self.numberofstops = numberofstops #number of points to connect
        self.mutatebest = mutatebest #wether the best path at each iteration should be mutated or not
        self.verbose = verbose #wether the best and worst paths for each iteration should be shown
        self.maxmen = maxmen #maximum number of specimen
        self.xymax = xymax #size of the "map"
        self.mutationrate = mutationrate # rate of mutation 0.1 is plenty

        #randomly initialize the targets
        self.targets = np.random.randint(xymax, size=(numberofstops, 2))
        #randomly initialize the specimen
        self.men = np.empty((maxmen, numberofstops), dtype = np.int32)
        for number in range(maxmen):
            tempman = np.arange(numberofstops, dtype = np.int32)
            np.random.shuffle(tempman)
            self.men[number] = tempman

        #find the best specimen of the first created
        self.best = np.array(self.getbestsalesmen())[...,0][0]


#Method that returns the best route at runtime
    def getbestsalesmen(self):
        #initiate a temporary order
        temporder = np.empty([len(self.men), 2], dtype = np.int32)
        #write the indexes of the route to temporder before ordering changes them
        for number in range(len(self.men)):
            temporder[number] = [number, 0,]
        #get length of path for all route
        for number in range(len(self.men)):
            templength = 0
            #get length of path
            for target in range(len(self.targets) - 1):
                diffx = abs(self.targets[self.men[number][target]][0] - self.targets[self.men[number][target + 1]][0])
                diffy = abs(self.targets[self.men[number][target]][1] - self.targets[self.men[number][target + 1]][1])
                diff = diffy + diffx
                templength = templength + diff
            #add length of way back
            diffx = abs(self.targets[self.men[number][0]][0] - self.targets[self.men[number][-1]][0])
            diffy = abs(self.targets[self.men[number][0]][1] - self.targets[self.men[number][-1]][1])
            diff = diffy + diffx
            templength = templength + diff
            #add length to order
            temporder[number][1] = templength
        #Sort route by length of path
        temporder = sorted(temporder, key=lambda x: -x[1])
        #return the best half of the route rounded up
        return temporder[int(len(temporder)/2):]

##https://pastmike.com/traveling-salesman-genetic-algorithm/#:~:text=The%20traveling%20salesman%20is%20an%20interesting%20problem%20to,What%20is%20the%20shortest%20route%20between%20the%20points%3F
