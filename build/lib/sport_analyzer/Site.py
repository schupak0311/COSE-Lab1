#!/usr/bin/python3 
class Site:
    def __init__(self):
        site_url = ""
        homeTeam_url = 0.0
        awayTeam_url = 0.0
        homeScore_url = 0.0
        awayScore_url = 0.0


    def setSiteUrl(self, data):
        self.site_url = data

    def sethomeTeam(self, data):
        self.homeTeam_url = data

    def setawayTeam(self,data):
        self.awayTeam_url = data

    def sethomeScore(self, data):
        self.homeScore_url = data

    def setawayScore(self, data):
        self.awayScore_url = data            

