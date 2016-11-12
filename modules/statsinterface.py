from stattlepy import Stattleship
import json
import Data

def getGamesList():
    New_query = Stattleship()
    Token = New_query.set_token('afbc9b6b0404332ed71e4726fba0ce40')
    Output = New_query.ss_get_results(sport='basketball',league='nba',ep='team_game_logs',season_id='nba-2015-2016',status='ended')

    totalGames = 0
    games = []

    for page in Output:
        logsList = page['team_game_logs']
        totalGames += len(logsList)
        for gameLog in logsList:
            games.append(Data.Game(gameLog))

    #print "%d games from last season added to returned list" % (totalGames)

    return games
