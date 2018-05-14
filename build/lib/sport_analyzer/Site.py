class Site:
    def __init__(self):
        self.site_url = ""
        self.homeTeam_url = 0.0
        self.awayTeam_url = 0.0
        self.homeScore_url = 0.0
        self.awayScore_url = 0.0

    def setSiteUrl(self, data):
        self.site_url = data

    def sethomeTeam(self, data):
        self.homeTeam_url = data

    def setawayTeam(self, data):
        self.awayTeam_url = data

    def sethomeScore(self, data):
        self.homeScore_url = data

    def setawayScore(self, data):
        self.awayScore_url = data
