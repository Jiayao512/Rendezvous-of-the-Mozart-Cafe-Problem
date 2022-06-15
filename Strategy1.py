###    STRATEGY 1    ###
###  Random Picking  ###

import numpy as np
import itertools as it

np.random.seed(1)

### Mozart Cafe problem without a river for n = 4 
'''
INPUT:
n: the number of cafés.
experiments: the number of trials of the simiulation to perform. In this case, this is 10,000.

OUTPUT:
count: a list in which the number of days to rendezvous are counted for each trial.
This list is used to compute the following:
- average: the average expected meeting time.
- maximum: the maximum number of days it took to rendezvous for this simulation.
- minimum: the minimum number of days it took to rendezvous for this simulation. 
'''
def random_pick(n,experiments):
    # This picking process is repeated multiple times and stored in a list
    count = []

    # All possible ways to label the cafes
    all_perm = list(it.permutations([i for i in range(1, n+1)]))

    for i in range(experiments):
        # The labels of the cafes may be different
        label1 = all_perm[np.random.randint(0,len(all_perm))]
        label2 = all_perm[np.random.randint(0,len(all_perm))]

        # player 1 picks a cafe, randomly, and similarly, for player 2.
        p1 = np.random.randint(1,n+1)    
        p2 = np.random.randint(1,n+1)    

        # To count the number of time units it takes for the two to find eachother.
        counter = 1 

        while label1.index(p1) != label2.index(p2):
            counter +=1
            p1 = np.random.randint(1,n+1)    
            p2 = np.random.randint(1,n+1)   
        
        count.append(counter)
    return(count)

# To test the random_pick function
def main():
    n = 4
    exp = 10000
    test1 = random_pick(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main()

### OUTPUT: 3.9946 35 1