import genetics as gene, statsinterface as si
import seatgeek as sg

Solution = None

def train():
    global Solution

    GameList = si.getGamesList()
    Solution = gene.getSolution(GameList)
    for attr in Solution.__dict__:
        print "{0:40} {1:10}".format(attr,Solution.__dict__[attr])


def predict():
    if Solution is None:
        print 'Must train first'
        return


    teams = raw_input('teams: ').split()

    team1 = si.getTeamStats(teams[0], True)
    team2 = si.getTeamStats(teams[1], True)

    score1 = gene.getGuess(Solution, team1)
    score2 = gene.getGuess(Solution, team2)

    print abs(score1 - score2) / (score1 + score2)

    if score1 > score2:
        print teams[0] + ' will win\n'
    elif score2 > score1:
        print teams[1] + ' will win\n'
    else:
        print 'Tie'

    return

if __name__ == '__main__':
    app.run()
    flags_dict = {"-v": 2}
    flags = 0

    while(1):
        #        try:
            print "t - Train\np - predict"
            user_input = raw_input().split()
            if(user_input[0] == "t"):
                train()
            elif(user_input[0] == "p"):
                predict()
                steams = raw_input('Enter the teams to find tickets!').split()
                sg.findGameBetweenTwoTeams(steams[0],steams[1])

            elif(user_input[0] == "x"):
                break
#        except:
#            print 'Try again\n'
#            continue
