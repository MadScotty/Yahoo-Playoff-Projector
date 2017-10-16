# Inserts data into webpage

def make_page(playoff_data, number_of_teams):

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
        </tr>
        """
    j = 0
    for i in range(0, number_of_teams):
        if playoff_data[j + 3] > 75:
            col = "#2d882d"
        elif playoff_data[j + 3] > 50:
            col = "#aaaa39"
        elif playoff_data[j + 3] > 25:
            col = "orange"
        else:
            col = "#7d1313"


        page += "       <tr>" \
                "           <td><img src=\"" + str(playoff_data[j]) + "\" style=\"width:25px;height:25px\">" + playoff_data[j + 1] + "</td>\n" \
                "           <td style =\"text-align:center\">" + str(playoff_data[j + 2]) + "</td>\n" \
                "           <td style =\"background-color:"+col+";text-align:center\">" + str(playoff_data[j + 3]) + "%</td>\n" \
                "       </td>"
        j += 4


    page+= "    </table>" \
           "    Results from simulating the end of the season 10k times.<br>" \
           "    Playoff percentage is the percentage of simulated seasons where a team makes the playoffs.<br>" \
           "    Coming soon: Playoff scenarios!" \
           "    </body>" \
           "</html>"

    with open("playoffs.html", "w") as file:
        file.write(page)