#!/usr/bin/python3 
import unittest
from sport_analyzer.Sitereader import getSitehtml
from sport_analyzer.Sitereader import getMatchResultsfromHtml
from sport_analyzer.Sitereader import createMatchResult

from sport_analyzer.Xmlprocess import getSitesfromXml
from sport_analyzer.Site import Site
import requests


class SitereaderTest(unittest.TestCase):
    def setUp(self):
        self.urls = []
        self.urls.append('/html/body/div[4]/div/div/div[3]/div/div[2]/div/div/a/span[2]/span/span')
        self.urls.append('/html/body/div[4]/div/div/div[3]/div/div[2]/div/div/a/span[4]/span/span')
        self.urls.append('/html/body/div[4]/div/div/div[3]/div/div/div/div/a/span[3]/span/span')
        self.urls.append('/html/body/div[4]/div/div/div[3]/div/div/div/div/a/span[3]/span/span[2]')

    def test_getSitesfromXml(self):
        sites = getSitesfromXml("./files/in.xml")
        site = sites[0]
        self.assertEqual(site.site_url, "http://www.skysports.com/football/fixtures-results")
        self.assertEqual(site.homeTeam_url,
                         self.urls[0])
        self.assertEqual(site.awayTeam_url,
                         self.urls[1])
        self.assertEqual(site.homeScore_url,
                         self.urls[2])
        self.assertEqual(site.awayScore_url,
                         self.urls[3])

    def test_getSitesfromXmlError(self):
        self.assertRaises(FileNotFoundError, getSitesfromXml, '')

    def test_getHtml(self):
        self.assertTrue(len(getSitehtml("http://www.skysports.com/football/fixtures-results")) > 0)
        self.assertRaises(requests.exceptions.ConnectionError, getSitehtml, 'http://d1d31f')

    def test_getMatchResultsfromHtml(self):
        html = getSitehtml("http://www.skysports.com/football/fixtures-results/22-April-2018")
        self.assertEqual(getMatchResultsfromHtml(html, self.urls[0]), "Arsenal")
        self.assertEqual(getMatchResultsfromHtml(html, self.urls[1]), "West Ham United")
        self.assertEqual(getMatchResultsfromHtml(html, self.urls[2]), "4")
        self.assertEqual(getMatchResultsfromHtml(html, self.urls[3]), "1")

    def test_createMatchResult(self):
        site = Site()
        site.setSiteUrl("http://www.skysports.com/football/fixtures-results/22-April-2018")
        site.sethomeTeam(self.urls[0])
        site.setawayTeam(self.urls[1])
        site.sethomeScore(self.urls[2])
        site.setawayScore(self.urls[3])
        expected_res = createMatchResult(site)
        self.assertEqual(expected_res.homeTeam, 'Arsenal')
        self.assertEqual(expected_res.awayTeam, 'West Ham United')
        self.assertEqual(expected_res.homeScore, '4')
        self.assertEqual(expected_res.awayScore, '1')


if __name__ == '__main__':
    unittest.main()
