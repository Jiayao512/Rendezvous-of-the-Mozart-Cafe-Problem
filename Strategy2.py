###   STRATEGY 2    ###
###      AW(4)      ###

import numpy as np
from random import choices
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
def AW(n,experiments):
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
        # To count the number of days the players have been searching or waiting.
        day = 0

        while label1.index(p1) != label2.index(p2):
            counter +=1                
            
            if day == 0 or day == (n-1):
                if day == (n-1):
                    day = 0

                lab1 = [x for x in label1 if x!=p1]
                lab2 = [x for x in label2 if x!=p2] 

                options = ["wait", "search"]
                choice1 = choices(options, weights=[1/n,1-(1/n)])
                choice2 = choices(options, weights=[1/n,1-(1/n)])

            day += 1

            # If the players do not meet on the first day, they choose to either wait or to search the other cafes for n-1 days. 
            if day != 0:
                if choice1 == ["search"]:
                    p1 = np.random.choice(lab1)    
                    lab1.remove(p1)
                if choice2== ["search"]:  
                    p2 = np.random.choice(lab2) 
                    lab2.remove(p2)  

        count.append(counter)
    return(count)

# To test the AW function
def main():
    n = 9
    exp = 10000
    test1 = AW(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main()

### OUTPUT 3.5937 28 1