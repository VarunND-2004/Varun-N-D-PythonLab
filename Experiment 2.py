"""
-------------------------------------------------------------------------------
EXPERIMENT NO: 2
NAME OF THE EXPERIMENT: Write a Program to implement control flow statements
                        and looping statements in python.
-------------------------------------------------------------------------------

PROBLEM STATEMENT:
Write a program to implement control flow statements and looping statements in python.

ALGORITHM:
STEP 1 : Start the program.
STEP 2 : Repeat the process for 5 players using a loop.
STEP 3 : Display a message asking the user to enter the details of the player.
STEP 4 : Read the following inputs from the user:
         > Player name
         > Runs scored
         > Balls faced
         > Wickets taken
         > Runs conceded while bowling
         > Number of overs bowled
         > Number of catches taken
STEP 5 : Calculate the strike rate using the formula: Strike Rate = (Runs ÷ Balls) × 100.
STEP 6 : Calculate the economy rate using the formula: Economy = Runs Conceded ÷ Overs Bowled.
STEP 7 : Determine the batting performance based on runs and strike rate.
STEP 8 : Determine the bowling performance based on wickets taken and economy rate.
STEP 9 : Determine the fielding performance based on the number of catches.
STEP 10 : Based on batting and bowling results, decide the all-rounder performance level.
STEP 11 : Display the player’s name, strike rate, economy rate, batting category,
          bowling category, fielding category, and all-rounder decision.
STEP 12 : Repeat the process until all 5 players are evaluated.
STEP 13 : Stop the program.

-------------------------------------------------------------------------------
"""

# --- SOURCE CODE ---

for player in range(1, 6):
    print("\n" + "="*30)
    print("Enter details for Player", player)
    print("="*30)

    name = input("Player Name: ")
    runs = int(input("Runs scored: "))
    balls = int(input("Balls faced: "))
    wickets = int(input("Wickets taken: "))
    runs_conceded = int(input("Runs conceded: "))
    overs = int(input("Overs bowled: "))
    catches = int(input("Catches taken: "))

    # Calculations
    strike_rate = (runs / balls) * 100
    economy_rate = runs_conceded / overs

    # Batting Status Logic
    if runs >= 50 and strike_rate >= 120:
        batting_status = "Excellent Batter"
    elif runs >= 30 and strike_rate >= 100:
        batting_status = "Good Batter"
    elif runs >= 20:
        batting_status = "Average Batter"
    else:
        batting_status = "Below Average Batter"

    # Bowling Status Logic
    if wickets >= 3 and economy_rate <= 6:
        bowling_status = "Excellent Bowler"
    elif wickets >= 2 and economy_rate <= 8:
        bowling_status = "Good Bowler"
    elif wickets >= 1:
        bowling_status = "Average Bowler"
    else:
        bowling_status = "Needs Improvement"

    # Fielding Status Logic
    if catches >= 2:
        fielding_status = "Outstanding Fielder"
    elif catches == 1:
        fielding_status = "Active Fielder"
    else:
        fielding_status = "Low Fielding Impact"

    # All-Rounder Status Logic
    if batting_status == "Excellent Batter" and bowling_status == "Excellent Bowler":
        all_rounder_status = "Star All-Rounder"
    elif batting_status == "Good Batter" and bowling_status == "Good Bowler":
        all_rounder_status = "Strong All-Rounder"
    elif batting_status == "Good Batter" or bowling_status == "Good Bowler":
        all_rounder_status = "Useful All-Rounder"
    else:
        all_rounder_status = "Needs Development"

    # Display Report
    print("\n--- Player Performance Report ---")
    print("Name:", name)
    print(f"Strike Rate: {strike_rate:.2f}")
    print(f"Economy Rate: {economy_rate:.2f}")
    print("Batting Performance:", batting_status)
    print("Bowling Performance:", bowling_status)
    print("Fielding Performance:", fielding_status)
    print("All-Rounder Rating:", all_rounder_status)

"""
-------------------------------------------------------------------------------
SAMPLE OUTPUT:
Enter details for Player 1
Player Name: HARDIK
Runs scored: 22
Balls faced: 20
Wickets taken: 4
... (Output continues for 5 players as shown in code execution) ...
-------------------------------------------------------------------------------
"""