import sys
import genetics as gene, statsinterface as si
import seatgeek as sg

Solution = gene.read()[0]

def train():
    global Solution

    GameList = si.getGamesList()
    Solution = gene.getSolution(GameList)
    for attr in Solution.__dict__:
        print "{0:40} {1:10}".format(attr,Solution.__dict__[attr])


def predict(teamName1=None, teamName2=None):
    team1 = si.getTeamStats(teamName1, True)
    team2 = si.getTeamStats(teamName2, True)

    score1 = gene.getGuess(Solution, team1)
    score2 = gene.getGuess(Solution, team2)

    print abs(score1 - score2) / (score1 + score2)

    if score1 > score2:
        print teamName1 + ' will win\n'
    elif score2 > score1:
        print teamName2 + ' will win\n'
    else:
        print 'Tie'

    return

if __name__ == '__main__':
    flags_dict = {"-v": 2}
    flags = 0

    if(sys.argv[1] == 'p'):
        team1=sys.argv[2]
        team2=sys.argv[3]
        predict(team1,team2)
        steams = raw_input('Enter the teams to find tickets!').split()
        sg.findGameBetweenTwoTeams(steams[0],steams[1])
    elif(sys.argv[1] == 't'):
        train()
