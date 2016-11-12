import genetics as gene, statsinterface as si

def train():
    GameList = si.getGamesList()
    Solution = gene.getSolution(GameList)
    for attr in Solution.__dict__:
        print "{0:40} {1:10}".format(attr,Solution.__dict__[attr])


def predict():
    pass


if __name__ == '__main__':
    flags_dict = {"-v": 2}
    flags = 0
    
    while(1):
        print "t - Train\np - predict"
        user_input = raw_input().split()
        if(user_input[0] == "t"):
            train()
        elif(user_input[0] == "p"):
            pass

