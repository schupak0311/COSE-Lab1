#!/usr/bin/python3
import requests
import urllib.error
from lxml import html
from events_analyzer.TeamStats import TeamStats
from events_analyzer.Xmlprocess import getSitesfromXml
from events_analyzer.Xmlprocess import writeSitesToXml


def getSitehtml(url):
    root = ""
    try:
        r = requests.get(url)
        root = html.fromstring(r.content)
    except urllib.error.URLError:
        print('Invalid URL({})'.format(url))
        raise
    return root


def getTeamStatsfromHtml(html, xpath):
    obj = ''
    try:
        obj = html.xpath(xpath)
    except RuntimeError:
        print("Html or xpath incorrect")
    return obj[0].text.strip()


def createTeamStats(site):
    html = getSitehtml(site.site_url)
    ex_rate = TeamStats(site.site_url,
                        getTeamStatsfromHtml(html, site.nameTeam_url))
    return ex_rate


# exs = []
# for ex in getSitesfromXml("files/in.xml"):
#     ex1 = createTeamStats(ex)
#     exs.append(ex1)

# writeSitesToXml(exs, "files/out.xml")
