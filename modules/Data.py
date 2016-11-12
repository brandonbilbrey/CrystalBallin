import random

class Game:
    def __init__(self, TeamName, Score):
        self.TeamName = TeamName
        self.Score = Score
        #self.IsHomeTeam = IsHomeTeam
        #self.TotalAssists = TotalAssists
        #self.AssistTurnoverRatio = AssistTurnOverRatio
        #self.BlockedTotal = BlockedTotal
        #self.BlocksTotal = BlocksTotal
        #self.CoachTechnicalFouls = CoachTechnicalFouls
        #self.Ejections = Ejections
        #self.FastBreakPoints = FastBreakPoints
        #self.FieldGoalsAttempted = FieldGoalsAttempted
        #self.FieldGoalsMade = FieldGoalsMade
        #self.FieldGoalsPercentage = FieldGoalsPercentage
        #self.FlagrantFouls = FlagrantFouls
        #self.FreeThrowsAttempted = FreeThrowsAttempted
        #self.FreeThrowsMade = FreeThrowsMade
        #self.FreeThrowsPercentage = FreeThrowsPercentage
        #self.PersonalFouls = PersonalFouls
        #self.PointsInPaint = PointsInPaint
        #self.PointsScoredOffTurnovers = PointsScoredOffTurnovers
        #self.ReboundsOffensive = ReboundsOffensive
        #self.ReboundsDefensive = ReboundsDefensive
        #self.ReboundsTotal = ReboundsTotal
        #self.SecondChancePoints = SecondChancePoints
        #self.StealsTotal = StealsTotal
        #self.TeamReboundsTotal = TeamReboundsTotal
        #self.TeamTurnoversTotal = TeamTurnoversTotal
        #self.TechnicalFouls = TechnicalFouls
        #self.ThreePointersAttempted = ThreePointersAttempted
        #self.ThreePointersMade = ThreePointersMade
        #self.ThreePointersPercentage = ThreePointersPercentage
        #self.TurnoversTotal = TurnoversTotal
        #self.TwoPointersAttempted = TwoPointersAttempted
        #self.TwoPointersMade = TwoPointersMade
        #self.TwoPointersPercentage = TwoPointersPercentage

class Solution:
    def __init__(self):
        self.IsHomeTeamWeight = randomWeight()
        self.TotalAssistsWeight = randomWeight()
        self.AssistTurnoverRatioWeight = randomWeight()
        self.BlockedTotalWeight = randomWeight()
        self.BlocksTotalWeight = randomWeight()
        self.CoachTechnicalFoulsWeight = randomWeight()
        self.EjectionsWeight = randomWeight()
        self.FastBreakPointsWeight = randomWeight()
        self.FieldGoalsAttemptedWeight = randomWeight()
        self.FieldGoalsMadeWeight = randomWeight()
        self.FieldGoalsPercentageWeight = randomWeight()
        self.FlagrantFoulsWeight = randomWeight()
        self.FreeThrowsAttemptedWeight = randomWeight()
        self.FreeThrowsMadeWeight = randomWeight()
        self.FreeThrowsPercentageWeight = randomWeight()
        self.PersonalFoulsWeight = randomWeight()
        self.PointsInPaintWeight = randomWeight()
        self.PointsScoredOffTurnoversWeight = randomWeight()
        self.ReboundsOffensiveWeight = randomWeight()
        self.ReboundsDefensiveWeight = randomWeight()
        self.ReboundsTotalWeight = randomWeight()
        self.SecondChancePointsWeight = randomWeight()
        self.StealsTotalWeight = randomWeight()
        self.TeamReboundsTotalWeight = randomWeight()
        self.TeamTurnoversTotalWeight = randomWeight()
        self.TechnicalFoulsWeight = randomWeight()
        self.ThreePointersAttemptedWeight = randomWeight()
        self.ThreePointersMadeWeight = randomWeight()
        self.ThreePointersPercentageWeight = randomWeight()
        self.TurnoversTotalWeight = randomWeight()
        self.TwoPointersAttemptedWeight = randomWeight()
        self.TwoPointersMadeWeight = randomWeight()
        self.TwoPointersPercentageWeight = randomWeight()


def randomWeight():
    random.seed()
    return random.uniform(0,1)


