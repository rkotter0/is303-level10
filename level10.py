# Riley Kotter
# IS 303 - Level #10 Assignment
# This program lets the user pick a college football season from cfb.csv
# and shows the teams from that season sorted into four win categories.

import pandas as pd

# Read the football data from the CSV file
df = pd.read_csv("cfb.csv")

# Ask the user which season they want to analyze
season_input = input("Enter a season to analyze: ")

# Make a list of every season that is in the file (no hard-coding)
seasons = []
for year in df["Season"]:
    if year not in seasons:
        seasons.append(year)

# Check that the user typed a number and that the season is in the file
if season_input.strip().isdigit() and int(season_input) in seasons:
    season = int(season_input)

    # Only keep the rows for the season the user picked,
    # sorted so the teams with the most wins show up first
    season_df = df[df["Season"] == season]
    season_df = season_df.sort_values(["Win", "Team"], ascending=[False, True])

    # Dictionary to organize the teams into the four win categories
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    # Loop through each team and put it in the right category
    for index, row in season_df.iterrows():
        # Team names look like "BYU (FBS Independent)", so remove the conference part
        team = row["Team"].rsplit(" (", 1)[0]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append(team)
        elif wins >= 8:
            categories["8-9 wins"].append(team)
        elif wins >= 6:
            categories["6-7 wins"].append(team)
        else:
            categories["Fewer than 6 wins"].append(team)

    # Display the results
    print()
    print("College Football Results for " + str(season))

    for category in categories:
        print()
        print(category + ":")
        if len(categories[category]) == 0:
            print("  (no teams)")
        else:
            for team in categories[category]:
                print("  " + team)
else:
    # Let the user know the season was not found
    print()
    print("Sorry, the season " + season_input + " was not found in the data.")
    print("Seasons available:", end=" ")
    for year in seasons:
        print(year, end=" ")
    print()
