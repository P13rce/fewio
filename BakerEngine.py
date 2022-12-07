import numpy as np
import pandas as pd
from Baker import Baker
# from scipy.stats import norm
# import matplotlib.pyplot as plt


# For Data Formating

baker_wins = {"Baker 1": 0, "Baker 2": 0, "Baker 3": 0, "Baker 4": 0, "Baker 5": 0, "Baker 6": 0,
              "Baker 7": 0, "Baker 8": 0, "Baker 9": 0, "Baker 10": 0, "Baker 11": 0, "Baker 12": 0}

week_elim_count = []  # Week of elimination for each baker
win_percentages = []  # Win percentage of each baker
BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8, 6)  # The weight of each baker in order
data = pd.DataFrame()


def intialize_data(baker_list):
    """Make Data ready to be displayed"""
    temp_week_count = []

    
    currentWeek = 1
    # Add Weeks 
    
    print(baker_list[0].weeks_eliminated)
    
    for baker in baker_list:
        win_percentages.append(baker.win_percentage)
        
        # print(baker.weeks_eliminated["Week 1"])
    for i in range (12):
        for baker in baker_list:
            temp_week_count.append(baker.weeks_eliminated["Week " + str(currentWeek)])
            
        print(temp_week_count)     
        if i < 11:
            temp_week_count = []   
            
        week_elim_count.append({"Week " + str(currentWeek): temp_week_count})
        currentWeek += 1
    


    # Finds the week of elimination and the win percentage for each baker
    # Then saves it into a global variable to be used when displaying data
    for baker in baker_list:
        win_percentages.append(baker.win_percentage)
        # print(baker.win_percentage)
        # print(baker.weeks_eliminated[0])
        # print({x: baker.weeks_eliminated for x in baker.weeks_eliminated})
        temp_week_count.append(baker.weeks_eliminated["Week 1"])
        # print(baker.win_percentage)
    week_elim_count.append(temp_week_count)



def pickVal(weight):
    """Get a random value corresponding to the weight of each baker"""
    return np.random.randint(0, weight)


def resetScores(baker_list_copy):
    """Reset the bakers score (Called every three rounds)"""
    for baker in baker_list_copy:
        baker.currentScore = 0


def calc_loss_week(baker_contestents, baker):
    currentWeek = "Week " + str(12 - len(baker_contestents))
    baker.weeks_eliminated[currentWeek] += 1


def simulate_wins(baker_list: list):
    currentWeek = 0

    baker_list_copy = baker_list.copy()

    # Runs the trial and will slowly remove bakers from baker_list_copy.
    while len(baker_list_copy) > 1:
        # Simulate the three challenges before an elimination
        for baker in baker_list_copy:
            for challenge in range(3):
                baker.currentScore += pickVal(baker.weight)

        # Variables used to find higest score
        highest_score = -1
        highest_score_baker = Baker(-1, "NULL")
        currentWeek += 1

        # Find the baker with the highest score
        for baker in baker_list_copy:
            if baker.currentScore > highest_score:
                highest_score = baker.currentScore
                highest_score_baker = baker

        # After finding the baker with the highest score, it is removed
        del baker_list_copy[baker_list_copy.index(highest_score_baker)]

        # Calculate week that baker was elimnated
        calc_loss_week(baker_list_copy, highest_score_baker)

    # Now that we have one contestent, they're the winner, increment win_count
    baker_wins[baker_list_copy[0].name] += 1


def calc_win_percentile(baker_list, num_epochs):
    """Find each baker's win percentage"""
    for baker in baker_list:
        # Rounds to 3 decimals
        baker.win_percentage = round(
            (baker_wins[baker.name] / num_epochs) * 100, 3)
    # baker.probability = baker_wins[baker.name]



        
def display_DataFrame():
    """Display the final data of all the simulation"""

    # DYNAMICALLY MAKE ELIM COUNT
    # print(week_elim_count)[0]
    # print(str(list(week_elim_count[0].keys())[0]))    
    # print(list(week_elim_count[0].values()))
    print(str(list(week_elim_count[0].keys())[0]))
    print(list(week_elim_count[0].values())[0])
    print()

    print(

        pd.DataFrame({"Bakers": list(baker_wins.keys()), 
                      "Wins": list(baker_wins.values()), "Win-Percentages": win_percentages,
                      str(list(week_elim_count[0].keys())[0]): list(week_elim_count[0].values())[0],
                     }
            ),

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
    """Run the simulation"""
    baker_list = []

    # Initialize baker
    for i in range(12):
        baker_list.append(Baker(BAKER_RANKS[0], ("Baker " + str(i + 1))))

    # Run each induvidual trial
    for i in range(epochs):
        # Print progress
        print(str(i) + " | " + str("{:.2f}".format(round((i / epochs) * 100, 2))) + "%")

        # Simulate round
        simulate_wins(baker_list)

    # Calculate data for all trials
    calc_win_percentile(baker_list, epochs)

    # Display final data
    intialize_data(baker_list)
    display_DataFrame()


if __name__ == '__main__':
    main()
