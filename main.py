# Yahoo! Fantasy Sports Playoff Projector by MadScotty
# WIP

import pull_data
import simulator
import make_page

# Adjust constants here
playoff_length = 3
num_playoff_teams = 6
simulations = 10000
number_of_teams = 12

# Grab data from Yahoo using Yahoo's API
league_data = pull_data.pull_data(playoff_length)

# Do the simulations
playoff_data = simulator.season_simulator(league_data, num_playoff_teams, simulations)

# Make a pretty html page with the results
make_page.make_page(playoff_data, len(playoff_data))