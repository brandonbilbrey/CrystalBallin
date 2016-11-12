import random

class Game:
    def __init__(self, gameStats):
        self.IsHomeTeam = gameStats["is_home_team"]
        self.TotalAssists = gameStats["assists_total"]
        self.AssistTurnoverRatio = gameStats["assists_turnover_ratio"]
        #self.BlockedTotal = BlockedTotal
        self.BlocksTotal = gameStats["blocks_total"]
        #self.CoachTechnicalFouls = CoachTechnicalFouls
        #self.Ejections = Ejections
        self.FastBreakPoints = gameStats["fast_break_points"]
        #self.FieldGoalsAttempted = FieldGoalsAttempted
        self.FieldGoalsMade = gameStats["field_goals_made"]
        self.FieldGoalsPercentage = gameStats["field_goals_percentage"]
        #self.FlagrantFouls = FlagrantFouls
        #self.FreeThrowsAttempted = FreeThrowsAttempted
        self.FreeThrowsMade = gameStats["free_throws_made"]
        self.FreeThrowsPercentage = gameStats["free_throws_percentage"]
        #self.PersonalFouls = PersonalFouls
        self.PointsInPaint = gameStats["points_in_paint"]
        #self.PointsScoredOffTurnovers = PointsScoredOffTurnovers
        self.ReboundsOffensive = gameStats["rebounds_offensive"]
        #self.ReboundsDefensive = ReboundsDefensive
        self.ReboundsTotal = gameStats["rebounds_total"]
        #self.SecondChancePoints = SecondChancePoints
        self.StealsTotal = gameStats["steals_total"]
        #self.TeamReboundsTotal = TeamReboundsTotal
        #self.TeamTurnoversTotal = TeamTurnoversTotal
        #self.TechnicalFouls = TechnicalFouls
        #self.ThreePointersAttempted = ThreePointersAttempted
        self.ThreePointersMade = gameStats["three_pointers_made"]
        self.ThreePointersPercentage = gameStats["three_pointers_percentage"]
        #self.TurnoversTotal = TurnoversTotal
        #self.TwoPointersAttempted = TwoPointersAttempted
        #self.TwoPointersMade = TwoPointersMade
        self.TwoPointersPercentage = gameStats["two_points_percentage"]

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
