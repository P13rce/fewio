import numpy as np
import pandas as pd
from Baker import Baker

# from scipy.stats import norm
# import matplotlib.pyplot as plt


# For Data Formating

baker_wins = {"Baker 1": 0, "Baker 2": 0, "Baker 3": 0, "Baker 4": 0, "Baker 5": 0, "Baker 6": 0,
              "Baker 7": 0, "Baker 8": 0, "Baker 9": 0, "Baker 10": 0, "Baker 11": 0, "Baker 12": 0}

week_elim_count = []
win_percentages = []
BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8, 6)
data = pd.DataFrame()


def intialize_data(baker_list):
    temp_week_count = []
    for baker in baker_list:
        win_percentages.append(baker.win_percentage)
        # print(baker.win_percentage)
        # print(baker.weeks_eliminated[0])
        # print({x: baker.weeks_eliminated for x in baker.weeks_eliminated})
        temp_week_count.append(baker.weeks_eliminated["Week 1"])
        # print(baker.win_percentage)
    week_elim_count.append(temp_week_count)


def pickVal(weight):
    return np.random.randint(0, weight)


def resetScores(baker_list_copy):
    for baker in baker_list_copy:
        baker.currentScore = 0


def calc_loss_week(baker_contestents, baker):
    currentWeek = "Week " + str(12 - len(baker_contestents))
    baker.weeks_eliminated[currentWeek] += 1


def simulate_wins(baker_list: list):
    currentWeek = 0

    baker_list_copy = baker_list.copy()

    while len(baker_list_copy) > 1:
        for baker in baker_list_copy:
            for challenge in range(3):
                baker.currentScore += pickVal(baker.weight)

        highest_score = -1
        highest_score_baker = Baker(-1, "NULL")
        currentWeek += 1

        for baker in baker_list_copy:
            if baker.currentScore > highest_score:
                highest_score = baker.currentScore
                highest_score_baker = baker
        del baker_list_copy[baker_list_copy.index(highest_score_baker)]

        # Calculate week that baker was elimnated
        calc_loss_week(baker_list_copy, highest_score_baker)

    # Now that we have one contestent, they're the winner, increment win_count
    baker_wins[baker_list_copy[0].name] += 1


def calc_win_percentile(baker_list, num_epochs):
    for baker in baker_list:
        print(baker.name)
        print(baker_wins[baker.name])

        # Rounds to 3 decimals
        baker.win_percentage = round(
            (baker_wins[baker.name] / num_epochs) * 100, 3)
    # baker.probability = baker_wins[baker.name]


def display_DataFrame():
    # DYNAMICALLY MAKE ELIM COUNT
    print(
        pd.DataFrame({"Bakers": list(baker_wins.keys()), "Wins": list(
            baker_wins.values()), "Win-Percentages": win_percentages,
                      "Week 1": week_elim_count[0],
                      #        "Week 2": week_elim_count[1],
                      #        "Week 3": week_elim_count[2],
                      #        "Week 4": week_elim_count[3],
                      #        "Week 5": week_elim_count[4],
                      #        "Week 6": week_elim_count[5],
                      #        "Week 7": week_elim_count[6],
                      #        "Week 8": week_elim_count[7],
                      #        "Week 9": week_elim_count[8],
                      #        "Week 10": week_elim_count[9],
                      #        "Week 11": week_elim_count[10],
                      #        "Week 12": week_elim_count[11],
                      }),
    )


def main():
    try:
        i: int = int(input("Please enter the amount of trials to run: "))
    except:
        return

    run(i)


def run(epochs: int):
    baker_list = []

    for i in range(12):
        baker_list.append(Baker(BAKER_RANKS[0], ("Baker " + str(i + 1))))

    for i in range(epochs):
        simulate_wins(baker_list)

    calc_win_percentile(baker_list, epochs)

    intialize_data(baker_list)
    display_DataFrame()


if __name__ == '__main__':
    main()
