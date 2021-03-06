###    STRATEGY 1    ###
###  Random Picking  ###

import numpy as np
import itertools as it

np.random.seed(1)

### Mozart Cafe problem with a river for n = 4
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
def random_pick_with(n,experiments):
    count = []

    # All possible ways to label the cafes
    all_perm = list(it.permutations([i for i in range(1, n+1)]))

    for i in range(experiments):
        # The labels of the cafes may be different
        label1 = all_perm[np.random.randint(0,len(all_perm))]
        label2 = all_perm[np.random.randint(0,len(all_perm))]
        
        # A coin is flipped for both players to decide at which side of the river to search.
        coin1 = np.random.randint(0,2)
        coin2 = np.random.randint(0,2)
        
        # player 1 picks a cafe, randomly, and similarly, for player 2. 
        if coin1 == 0:
            p1 = np.random.choice(list(label1[:round(n/2)]))
        else:
            p1 = np.random.choice(list(label1[round(n/2):]))

        if coin2 == 0:
            p2 = np.random.choice(list(label2[:round(n/2)]))  
        else:
            p2 = np.random.choice(list(label2[round(n/2):]))

        # To count the number of time units it takes for the two to find eachother.
        counter = 1 

        while label1.index(p1) != label2.index(p2):
            counter +=1

            # The coin is only flipped after n/2 time units, so for n = 4, this means on Day 1, Day 3 etc.
            if counter%round(n/2) == 1:
                coin1 = np.random.randint(0,2)
                coin2 = np.random.randint(0,2)

            if coin1 == 0:
                p1 = np.random.choice(list(label1[0:round(n/2)]))
            else:
                p1 = np.random.choice(list(label1[round(n/2):]))

            if coin2 == 0:
                p2 = np.random.choice(list(label2[0:round(n/2)]))  
            else:
                p2 = np.random.choice(list(label2[round(n/2):])) 
        
        count.append(counter)
    return(count)

# To test the random_pick_with function
def main():
    n = 4
    exp = 10000
    test1 = random_pick_with(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main() 

### OUTPUT: 4.6556 36 1