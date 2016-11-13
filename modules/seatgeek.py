from seatgeek_api import event

def findGameBetweenTwoTeams(team1,team2):
    games = event.get_event_data_for_query(team1 + " " + team2)

    print "Games found for the teams: \n";
    for game in games:
        printGameInfo(game)

def printGameInfo(game):
    gameInfo = ""
    gameInfo += game.title
    gameInfo += " Average price = "
    gameInfo += unicode(game.average_price)
    gameInfo += " at "
    gameInfo += unicode(game.datetime_local)

    print gameInfo

findGameBetweenTwoTeams("bulls","wizards")
