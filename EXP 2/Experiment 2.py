
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


    strike_rate = (runs / balls) * 100
    economy_rate = runs_conceded / overs

    if runs >= 50 and strike_rate >= 120:
        batting_status = "Excellent Batter"
    elif runs >= 30 and strike_rate >= 100:
        batting_status = "Good Batter"
    elif runs >= 20:
        batting_status = "Average Batter"
    else:
        batting_status = "Below Average Batter"

    if wickets >= 3 and economy_rate <= 6:
        bowling_status = "Excellent Bowler"
    elif wickets >= 2 and economy_rate <= 8:
        bowling_status = "Good Bowler"
    elif wickets >= 1:
        bowling_status = "Average Bowler"
    else:
        bowling_status = "Needs Improvement"

   
    if catches >= 2:
        fielding_status = "Outstanding Fielder"
    elif catches == 1:
        fielding_status = "Active Fielder"
    else:
        fielding_status = "Low Fielding Impact"

  
    if batting_status == "Excellent Batter" and bowling_status == "Excellent Bowler":
        all_rounder_status = "Star All-Rounder"
    elif batting_status == "Good Batter" and bowling_status == "Good Bowler":
        all_rounder_status = "Strong All-Rounder"
    elif batting_status == "Good Batter" or bowling_status == "Good Bowler":
        all_rounder_status = "Useful All-Rounder"
    else:
        all_rounder_status = "Needs Development"

    print("\n--- Player Performance Report ---")
    print("Name:", name)
    print(f"Strike Rate: {strike_rate:.2f}")
    print(f"Economy Rate: {economy_rate:.2f}")
    print("Batting Performance:", batting_status)
    print("Bowling Performance:", bowling_status)
    print("Fielding Performance:", fielding_status)
    print("All-Rounder Rating:", all_rounder_status)
