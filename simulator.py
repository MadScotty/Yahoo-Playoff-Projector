# Holy iteration, Batman!

import random

def season_simulator(teams, num_playoff_teams, simulations):
    
    # Add new info to dicts
    for i in range(0, len(teams)):
        teams[i].update({"total_wins" : teams[i]["wins"]})
        teams[i].update({"total_berths" : 0})
        teams[i].update({"season_wins" : 0})

    # For each season
    for season in range(0, simulations):
        # Reset wins for the new season
        for i in teams:
            i["season_wins"] = i["wins"]

        # For each week
        for week in range(0, len(teams[0]["rem_sched"])):
            # Populate matchup array as ...[a,b]... where a and b are the indexes of competing teams for the week
            matchup = []
            for i in range(0, len(teams)):
                if any(i in a for a in matchup):
                    continue
                else:
                    for j in range(0, len(teams)):
                        if teams[i]["rem_sched"][week] == (teams[j]["name"]):
                            opponent = j
                            break
                    matchup.append([i, opponent])

            # Simulate each matchup        
            for i in range(0, 6):
                odds_for_team_zero = teams[matchup[i][0]]["ppg"] / (teams[matchup[i][0]]["ppg"] + teams[matchup[i][1]]["ppg"]) * 100
                # Check to see who won
                if random.randint(1,100) < odds_for_team_zero:
                    teams[matchup[i][0]]["season_wins"] += 1
                else:
                    teams[matchup[i][1]]["season_wins"] += 1

        # Calculate end of season scores

        # Check each team to see if they made the playoffs        
        for i in teams:
            teams_above = 0
            for j in teams:
                if i["season_wins"] <= j["season_wins"]:
                    if i["season_wins"] == j["season_wins"] and i["ppg"] > j["ppg"]:
                        continue
                    teams_above += 1
            if teams_above < num_playoff_teams:
                i["total_berths"] += 1

        # Update W-L totals
        for i in teams:
            i["total_wins"] += i["season_wins"]

    for i in teams:
        i.update({"avg_wins" : float("{0:.1f}".format(i["total_wins"] / simulations))})
        pct = ((i["total_berths"]) / simulations) * 100
        i.update({"playoff_percentage" : float("{0:.1f}".format(pct))})


    # Sort teams by playoff percentage
    sorted_teams = sorted(teams, key=lambda x: x["playoff_percentage"], reverse=True)

    return sorted_teams