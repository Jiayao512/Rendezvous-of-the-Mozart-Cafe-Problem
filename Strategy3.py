###   STRATEGY 3    ###
###    Markstart    ###

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
def markstart(n,experiments):
    # This picking process is repeated multiple times and stored in a list
    count = []

    # All possible ways to label the cafes
    all_perm = list(it.permutations(np.arange(1,5)))

    for i in range(experiments):
        # The labels of the cafes may be different
        label1 = list(all_perm[np.random.randint(0,len(all_perm))])
        label2 = list(all_perm[np.random.randint(0,len(all_perm))])

        # player 1 picks a cafe, randomly, and similarly, for player 2. Then, at the first one the mark is placed.
        p1 = np.random.randint(1,n+1)    
        p2 = np.random.randint(1,n+1) 

        # It is assumed that the players never return to a cafe with a mark.
        lab1 = [x for x in label1 if x!=p1]
        lab2 = [x for x in label2 if x!=p2] 

        mark1 = label1.index(p1)
        mark2 = label2.index(p2)

        # To count the number of time units it takes for the two to find eachother.
        counter = 1 
        
        while label1.index(p1) != label2.index(p2):
            counter +=1
            p1 = np.random.choice(lab1)   
            p2 = np.random.choice(lab2) 

            if label1.index(p1) == mark2:
                lab1.remove(p1)
            if label2.index(p2) == mark1:
                lab2.remove(p2)

        count.append(counter)
    return(count)

# To test the mark function
def main():
    n = 4
    exp = 10000
    test1 = markstart(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main() 

### OUTPUT 3.275 16 1