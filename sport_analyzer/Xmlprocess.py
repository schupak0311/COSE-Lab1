#!/usr/bin/python3
import xml.etree.ElementTree as ET
from lxml import etree
from sport_analyzer.Site import Site


def getSitesfromXml(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        sites = []
        for child in root:
            site = Site()
            for siteinfo in child:
                if siteinfo.tag == "Url":
                    site.setSiteUrl(siteinfo.text)
                elif siteinfo.tag == "Match":
                    for match in siteinfo:
                        if match.tag == "HomeTeam":
                            site.sethomeTeam(match.text)
                        elif match.tag == "AwayTeam":
                            site.setawayTeam(match.text)
                        elif match.tag == "HomeTeamScore":
                            site.sethomeScore(match.text)
                        elif match.tag == "AwayTeamScore":
                            site.setawayScore(match.text)       
            sites.append(site)
    except FileNotFoundError:
        print("Such file doesn't exist!")
        raise
    return sites


def writeSitesToXml(data, file):
    root = etree.Element("xml")
    doc = etree.SubElement(root, "results")
    for i in data:
        eventName = etree.SubElement(doc, "Match")
        etree.SubElement(eventName, "Url").text = i.site_url
        match = etree.SubElement(eventName, "result")
        etree.SubElement(match, "HomeTeam").text = i.homeTeam
        etree.SubElement(match, "AwayTeam").text = i.awayTeam
        etree.SubElement(match, "HomeTeamScore").text = i.homeScore
        etree.SubElement(match, "AwayTeamScore").text = i.awayScore
    tree = etree.ElementTree(root)
    tree.write(file, pretty_print=True)
