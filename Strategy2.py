###   STRATEGY 2    ###
###      AW(4)      ###

import numpy as np
from random import choices
import itertools as it

np.random.seed(1)

### Mozart Cafe problem without a river for n = 4
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
    n = 4
    exp = 10000
    test1 = AW(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main()

### OUTPUT 3.5937 28 1

### Mozart Cafe problem with a river for n = 4
def AW_with(n,experiments):
    # This picking process is repeated multiple times 
    # and stored in a list
    count = []

    # All possible ways to label the cafes
    all_perm = list(it.permutations([i for i in range(1, n+1)]))

    for i in range(experiments):
        # The labels of the cafes may be different
        label1 = all_perm[np.random.randint(0,len(all_perm))]
        label2 = all_perm[np.random.randint(0,len(all_perm))]

        # Choose a river side
        coin1 = np.random.randint(0,2)
        coin2 = np.random.randint(0,2)
        if coin1 == 0:
            p1 = np.random.choice(label1[:round(n/2)])
        elif coin1 == 1:    
            p1 = np.random.choice(label1[round(n/2):])

        if coin2 == 0:
            p2 = np.random.choice(label2[:round(n/2)])
        elif coin2 == 1:
            p2 = np.random.choice(label2[round(n/2):])

        # To count the number of time units it takes for the two to find eachother.
        counter = 1 
        # To count the number of days the players have been searching or waiting.
        day = 0

        while label1.index(p1) != label2.index(p2):
            counter += 1

            if day == 0 or day == max(len(label1[:round(n/2)])-1, len(label1[round(n/2):])-1):
                if day == max(len(label1[:round(n/2)])-1, len(label1[round(n/2):])-1):
                    day = 0
                    coin1 = np.random.randint(0,2)
                    coin2 = np.random.randint(0,2)

                if coin1 == 0:
                    lab1 = [x for x in label1[:round(n/2)] if x!=p1]
                elif coin1 == 1:    
                    lab1 = [x for x in label1[round(n/2):] if x!=p1]

                if coin2 == 0:
                    lab2 = [x for x in label2[:round(n/2)] if x!=p2]  
                elif coin2 == 1:
                    lab2 = [x for x in label2[round(n/2):] if x!=p2] 

                options = ["wait", "search"]
                if coin1 == 1 and len(label1[round(n/2):]) == 1:
                    choice1 = ["wait"]
                elif coin1 == 0 or len(label1[round(n/2):]) != 1:
                    choice1 = choices(options, weights=[1/round(n/2),1-(1/round(n/2))])
                
                if coin2 == 1 and len(label2[round(n/2):]) == 1:
                    choice2 = ["wait"]
                elif coin2 == 0 or len(label2[round(n/2):]) != 1:
                    choice2 = choices(options, weights=[1/round(n/2),1-(1/round(n/2))])
            
            day += 1

            if day != 0:
                if choice1 == ["search"]:
                    p1 = np.random.choice(lab1)    
                    lab1.remove(p1)
                if choice2 == ["search"]:  
                    p2 = np.random.choice(lab2) 
                    lab2.remove(p2)

        count.append(counter)
    return(count)

# To test the AW_with function
def main():
    n = 4
    exp = 10000
    test1 = AW_with(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main() 

### OUTPUT 4.6919 37 1