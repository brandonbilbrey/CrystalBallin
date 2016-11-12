from Data import Game, Solution, randomWeight
import random

def getGuess(solution, data):
    total = 0
    for prop in data.__dict__:
        total += solution.__dict__[prop + "Weight"] * data.__dict__[prop]

def getFitness(solution, data):
    return 1 / abs(getGuess(solution, data) - data.score)

def mate(sol1, sol2, data):
    random.seed()

    returnSol = Solution()

    for prop in returnSol.__dict__:
        returnSol.__dict__[prop] = sol1.__dict__[prop] if (rand() % 2 == 0) else sol2.__dict__[prop]

def mutate(sol, prob = None):
    if prob == None:
        prob = 0.9

    if randomWeight() <= prob / 4:
        for prop in sol.__dict__:
            sol.__dict__[prop] = randomWeight()

    for prop in sol.__dict__:
        if randomWeight() <= prob:
            sol.__dict__[prop] = randomWeight()

    return sol

def rouletteSelect(sols, data):
    weight_sum = 0
    for sol in sols :
        weight_sum += getFitness(sol, data)

    value = randomWeight() * weight_sum

    for sol in sols:
        value -= getFitness(sol, data)
        if value <= 0:
            return sol
    return sols[-1]

def getNewGen(parents, data):
    children = []
    for i in range(len(parents)):
        parent1 = rouletteSelect(parents, data)
        parent2 = rouletteSelect(parents, data)
        
        child = mate(parent1, parent2, data)
        children.append(child)

    return children

def getSolution(gameList):
    # Create initial random solutions.
    solutions = []
    for i in range(30):
        solutions.append(Solution())

    for i in range(1000):
        for game in gameList:
            solutions = getNewGen(solutions, game)

