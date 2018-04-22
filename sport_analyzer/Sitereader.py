#!/usr/bin/python3
import requests
import urllib.error
from lxml import html
from sport_analyzer.MatchResults import MatchResults
from sport_analyzer.Xmlprocess import getSitesfromXml
from sport_analyzer.Xmlprocess import writeSitesToXml


def getSitehtml(url):
    root = ""
    try:
        r = requests.get(url)
        root = html.fromstring(r.content)
    except urllib.error.URLError:
        print('Invalid URL({})'.format(url))
        raise
    return root


def getMatchResultsfromHtml(html, xpath):
    obj = ''
    try:
        obj = html.xpath(xpath)
    except RuntimeError:
        print("Html or xpath incorrect")
    return obj[0].text.strip()


def createMatchResult(site):
    html = getSitehtml(site.site_url)
    result = MatchResults(site.site_url,
                           getMatchResultsfromHtml(html, site.homeTeam_url),
                           getMatchResultsfromHtml(html, site.awayTeam_url),
                           getMatchResultsfromHtml(html, site.homeScore_url),
                           getMatchResultsfromHtml(html, site.awayScore_url))
    return result


# arr = []
# for i in getSitesfromXml("files/in.xml"):
#     res = createMatchResult(i)
#     arr.append(res)

# writeSitesToXml(arr, "files/out.xml")
