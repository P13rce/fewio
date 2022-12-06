import numpy as np
import pandas as pd
from Baker import Baker
# import matplotlib.pyplot as plt

BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8, 6)
winners = []
def pickVal(weight):
    return np.random.randint(0,weight)


def resetScores(baker_list):
    for baker in baker_list:
        baker.currentScore = 0
    
def simulate(baker_list:list):
    while len(baker_list) > 1:
        for baker in baker_list:
            for challenge in range(3):
                baker.currentScore += pickVal(baker.weight)
        highest_score_index = -1
        highest_score = -1
        highest_score_baker = Baker(-1, "NULL")
        
        for baker in baker_list:
            if baker.currentScore > highest_score:
                highest_score = baker.currentScore
                highest_score_baker = baker
        del baker_list[baker_list.index(highest_score_baker)]
        resetScores(baker_list)

    winners.append(baker_list[0].name)

    
def main():
    try:
        i:int = int(input("Please enter the amount of trials to run: "))
    except:
        return

    run(i)
def run(epochs:int):

    for i in range(epochs):
        baker_list = []
        for j in range(12):
            baker_list.append(Baker(BAKER_RANKS[j],("Baker " + str(j))))
        
        simulate(baker_list)
    data = pd.DataFrame({"Winner": winners})


if __name__ == '__main__':
    main()