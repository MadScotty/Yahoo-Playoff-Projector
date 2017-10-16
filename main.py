import simulator
import pull_data
import make_page

# Adjust stuff here
playoff_length = 3
num_playoff_teams = 6
simulations = 10000
number_of_teams = 12

league_data = pull_data.pull_data(playoff_length)

playoff_data = simulator.season_simulator(league_data, num_playoff_teams, simulations)

make_page.make_page(playoff_data, int(len(playoff_data) / 4))