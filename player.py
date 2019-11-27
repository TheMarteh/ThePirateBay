class player:

    def __init__ (self, name, cannons, munten, isalive):
        self.name = name
        self.cannons = cannons
        self.munten = munten
        self.isalive = isalive

    def playerDeath(self):
        player.isalive = False

    def calculateScore(self):
        self.score = self.cannons + self.munten

