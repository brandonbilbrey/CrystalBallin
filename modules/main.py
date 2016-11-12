import genetics, statsinterface

if __name__ == '__main__':
    flags_dict = {"-v": 2}
    flags = 0
    
    while(1):
        print("t - Train\np - predict")
        user_input = input().split()
        if(user_input[0] == 't'):
            train()
        elif(user_input[0] == 'p'):
            pass


def train():
    GameList = getGamesList()
    Solution = getSolution(GameList)
    for attr, val in Solution.__dict__:
        print "{0:40} {1:10}".format(attr,val)

                
def predict():
    pass
