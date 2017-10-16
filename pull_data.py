# Voithed Playoff Projector

import myql
import json
from myql.utils import pretty_json
from yahoo_oauth import OAuth1
import simulator

def pull_data(playoff_length):

    # Authenticate
    oauth = OAuth1(None, None, from_file='creds.json')
    yql = myql.MYQL(format='json', oauth = oauth)

    if not oauth.token_is_valid():
        oauth.refresh_access_token()

    # Pull league standings data and send to the json parser
    resp = yql.raw_query('select * from fantasysports.leagues.standings where league_key="nfl.l.553162"')
    league_standings = json.loads(resp.content)

    # Grab week data from json
    current_week = int(league_standings["query"]["results"]["league"]["current_week"])
    end_week = int(league_standings["query"]["results"]["league"]["end_week"]) - (playoff_length)
    remaining_weeks = end_week - current_week + 1

    # Pull league schedules from remaining weeks from server and send to json parser
    schedules = []
    for i in range(current_week, end_week + 1):
        resp = yql.raw_query("select * from fantasysports.leagues.scoreboard where league_key='nfl.l.553162' and week='" + str(i) + "'")
        schedules.append(json.loads(resp.content))

    #----------------------------
    # Load all team data
    #----------------------------

    teams = []
    number_of_teams = int(league_standings["query"]["results"]["league"]["num_teams"])

    # Add owners and fill array indices with dicts
    for i in range(0, number_of_teams):
        teams.append({"name": str(league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["name"])})

    # Fill in rest of data
    # Oh god I know this is ugly and ungraceful, please forgive me future me when you go to fix this
    for i in range(0, number_of_teams):

        # Add names of remaining opponents
        rem_sched = []
        for j in range(0, len(schedules)):
            matchup_iterator = 0
            matchup_pos = -1
            while matchup_iterator <= 6:
                if schedules[j]["query"]["results"]["league"]["scoreboard"]["matchups"]["matchup"][matchup_iterator]["teams"]["team"][0]["name"] == teams[i]["name"]:
                    matchup_pos = 1
                    break
                elif schedules[j]["query"]["results"]["league"]["scoreboard"]["matchups"]["matchup"][matchup_iterator]["teams"]["team"][1]["name"] == teams[i]["name"]:
                    matchup_pos = 0
                    break
                else:
                    matchup_iterator += 1

            rem_sched.append(schedules[j]["query"]["results"]["league"]["scoreboard"]["matchups"]["matchup"][matchup_iterator]["teams"]["team"][matchup_pos]["name"])

        # Format ppg (points per game) as a two point float
        try:
            ppg = float(league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["team_points"]["total"])
            ppg /= current_week - 1
            ppg = float("{0:.2f}".format(ppg))
        except ZeroDivisionError:
            ppg = 0

        # Add the rest of data
        teams[i].update({"icon" : league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["team_logos"]["team_logo"]["url"]})
        teams[i].update({"points" : float(league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["team_points"]["total"])})
        teams[i].update({"wins" : int(league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["team_standings"]["outcome_totals"]["wins"])})
        teams[i].update({"losses" : int(league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["team_standings"]["outcome_totals"]["losses"])})
        teams[i].update({"ties" : int(league_standings["query"]["results"]["league"]["standings"]["teams"]["team"][i]["team_standings"]["outcome_totals"]["ties"])})
        teams[i].update({"ppg" : ppg})
        teams[i].update({"rem_sched" : rem_sched})

    return teams