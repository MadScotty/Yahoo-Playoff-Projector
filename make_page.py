# Inserts data into webpage
from datetime import date

def make_page(playoff_data, number_of_teams):

    today = str(date.today())

    page = """<!DOCTYPE html>
    <html>
        <head>
            <style>
                table{
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 50%;
                }

                td, th {
                border: 1px solid #eeeeee;
                text-align: left;
                padding: 8px
                }

                tr:nth-child(even) {
                background-color: #dddddd;
                }
            </style>
        </head>
    <body>
    <table>
        <tr>
            <th>Team Name</th>
            <th style="text-align:center">Avg. Wins</th>
            <th style="text-align:center">Playoff Odds</th>
        </tr>"""
        
    for i in range(0, number_of_teams):
        if playoff_data[i]["playoff_percentage"] > 75:
            col = "#2d882d"
        elif playoff_data[i]["playoff_percentage"] > 50:
            col = "#aaaa39"
        elif playoff_data[i]["playoff_percentage"] > 25:
            col = "orange"
        else:
            col = "#ff4d4d"

        page += "       <tr>\n" \
                "           <td><img src=\"" + str(playoff_data[i]["icon"]) + "\" style=\"width:25px;height:25px\">" + playoff_data[i]["name"] + "</td>\n" \
                "           <td style =\"text-align:center\">" + str(playoff_data[i]["avg_wins"]) + "</td>\n" \
                "           <td style =\"background-color:"+col+";text-align:center\">" + str(playoff_data[i]["playoff_percentage"]) + "%</td>\n" \
                "       </td>\n"

    page+= "    </table>\n" \
           "    <b>Last updated:</b> " + today + "<br>\n" \
           "    Results from simulating the end of the season 10k times.<br>\n" \
           "    Playoff percentage is the percentage of simulated seasons where a team makes the playoffs.<br>\n" \
           "    <b>Coming soon:</b> Playoff clinch/elimination scenarios!<br>\n" \
           "    <b><a href=\"https://github.com/MadScotty/Yahoo-Playoff-Projector\">Source</a>\n" \
           "    </body>\n" \
           "</html>"

    with open("playoffs.html", "w") as file:
        file.write(page)