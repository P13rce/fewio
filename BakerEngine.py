import numpy as np
import pandas as pd
import Baker

BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8, 6)

def pickVal(weight):
    return np.random.randint(0,weight)

def simulate(baker_list:list):
    while len(baker_list) > 1:
        for baker in baker_list:
            for challenge in range(3):
                baker.currentScore += pickVal(baker.weight)
        highest_score_index = -1
        highest_score = -1
        highest_score_baker = null
        run_amount = 0
        for baker in baker_list:
            if baker.currentScore > highest_score:
                highest_score = baker.currentScore
                highest_score_baker = baker
        
def main():
    try:
        i:int = int(input("Please enter the amount of trials to tun: "))
    except:
        return

    run(i)
def run(epochs:int):

    for i in range(epochs):
        baker_list = []
        for j in range(12):
            baker_list.append(Baker(BAKER_RANKS[j], "Baker " + str(j)))

        startChallenges(baker_list)





if __name__ == '__main__':
    main()