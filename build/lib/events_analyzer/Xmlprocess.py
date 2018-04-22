#!/usr/bin/python3
import xml.etree.ElementTree as ET
from lxml import etree
from events_analyzer.Site import Site


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
                elif siteinfo.tag == "FirstTeam":
                    for buy in siteinfo:
                        if buy.tag == "Name":
                            site.setnameTeam(buy.text)

            sites.append(site)
    except FileNotFoundError:
        print("Such file doesn't exist!")
        raise
    return sites


def writeSitesToXml(data, file):
    root = etree.Element("xml")
    doc = etree.SubElement(root, "teams results")
    for i in data:
        bankName = etree.SubElement(doc, "site")
        etree.SubElement(bankName, "Url").text = i.site_url
        buy = etree.SubElement(bankName, "FirstTeam")
        etree.SubElement(buy, "Name").text = i.buyRub
    tree = etree.ElementTree(root)
    tree.write(file, pretty_print=True)
