###   STRATEGY 3    ###
###    Markstart    ###

import numpy as np
import itertools as it

np.random.seed(1)

### Mozart Cafe problem without a river for n = 4
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

### Mozart Cafe problem with a river for n = 4
def markstart_with(n,experiments):
    # This picking process is repeated multiple times and stored in a list
    count = []

    # All possible ways to label the cafes
    all_perm = list(it.permutations([i for i in range(1, n+1)]))

    for i in range(experiments):
        # The labels of the cafes may be different
        label1 = list(all_perm[np.random.randint(0,len(all_perm))])
        label2 = list(all_perm[np.random.randint(0,len(all_perm))])

        lab1_0 = list(label1[0:round(n/2)])
        lab1_1 = list(label1[round(n/2):])
        lab2_0 = list(label2[0:round(n/2)])
        lab2_1 = list(label2[round(n/2):])

        # A coin is flipped for both players to decide at which side of the river to search.
        coin1 = np.random.randint(0,2)
        coin2 = np.random.randint(0,2)

        # player 1 picks a cafe, randomly, and similarly, for player 2. Then, at the first one the mark is placed.

        # It is assumed that the players never return to a cafe with a mark.
        if coin1 == 0:
            p1 = np.random.choice(lab1_0)
            lab1_0.remove(p1)
        else:
            p1 = np.random.choice(lab1_1)
            lab1_1.remove(p1)

        if coin2 == 0:
            p2 = np.random.choice(lab2_0)  
            lab2_0.remove(p2)
        else:
            p2 = np.random.choice(lab2_1)
            lab2_1.remove(p2)

        mark1 = label1.index(p1)
        mark2 = label2.index(p2)

        # To count the number of time units it takes for the two to find eachother.
        counter = 1 
        
        while label1.index(p1) != label2.index(p2):
            counter +=1

            if len(lab1_0) == 0:
                coin1 = 1
                p1 = np.random.choice(lab1_1)
            elif len(lab1_1) == 0:
                coin1 = 0
                p1 = np.random.choice(lab1_0)
            else: 
                if coin1 == 0:
                    p1 = np.random.choice(lab1_0)
                if coin1 == 1:
                    p1 = np.random.choice(lab1_1)

            if len(lab2_0) == 0:
                p2 = np.random.choice(lab2_1)
                coin2 = 1
            elif len(lab2_1) == 0:
                coin2 = 0
                p2 = np.random.choice(lab2_0)
            else: 
                if coin2 == 0:
                    p2 = np.random.choice(lab2_0)
                if coin2 == 1:
                    p2 = np.random.choice(lab2_1)

            if label1.index(p1) == mark2:
                if len(lab1_0) != len(label1[0:round(n/2)])-2 and p1 in lab1_0:
                    lab1_0.remove(p1)
                elif len(lab1_1) != len(label1[round(n/2):])-2 and p1 in lab1_1:
                    lab1_1.remove(p1)

            if label2.index(p2) == mark1:
                if len(lab2_0) != len(label2[0:round(n/2)])-2 and p2 in lab2_0:
                    lab2_0.remove(p2)
                elif len(lab2_1) != len(label2[round(n/2):])-2 and p2 in lab2_1:
                    lab2_1.remove(p2)

            if len(lab1_0) != 0 and len(lab1_1) != 0:
                coin1 = np.random.randint(0,2)

            if len(lab2_0) != 0 and len(lab2_1) != 0:
                coin2 = np.random.randint(0,2)

        count.append(counter)
    return(count)

# To test the markstart_with function
def main():
    n = 4
    exp = 10000 
    test1 = markstart_with(n,exp)
    average = np.mean(test1)
    maximum = np.max(test1)
    minimum = np.min(test1)
    print(average,maximum,minimum)
main() 

### OUTPUT 3.7138 17 1