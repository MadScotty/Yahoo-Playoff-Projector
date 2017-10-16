# Calculates elimination/clinching scenarios for the current week

def playoff_scenario(teams):
    # Add data to teams list
    rem_weeks = len(teams[0]["rem_sched"])
    

    for i in teams:
        i.update({"can_clinch" : False})
        i.update({"can_elim" : False})

