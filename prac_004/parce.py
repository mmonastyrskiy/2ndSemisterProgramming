import requests as r
from bs4 import BeautifulSoup as bs 
import mysql.connector as conn
import os
import configparser
import logging
import re
import colorama as color 

goods = []

class NotOKResponseCode(Exception):
    def __init__(self,message):
        self.message = message
        self.code = code
        self.data = data

CONFIG_FILE = "config.ini"

logging.basicConfig(filename='access.log')
logging.basicConfig(format='%(asctime)s %(message)s')

color.init(autoreset=True)

try:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)


    host = config.get("DEFAULT","host")
    dbname = config.get("DEFAULT","dbname")
    login = config.get("DEFAULT","login")
    password = config.get("DEFAULT","password")

except Exception:
    print("Error reading configuration file")

def GetDataFromURL(url: str) -> str:
    response = r.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise NotOKResponseCode(f"Something is wrong with the url:{url}, page returned code: {status_code}")

def ParceStore77Net_Sections(url):
    try:
        resp = GetDataFromURL(url)
    except NotOKResponseCode:
        print(color.Fore.RED + "Seems like host is down, check manually")
    soup = bs(resp,"lxml")
    sections = soup.find_all("ul",class_ = "catalog_menu_sub_third")
    #print(sections)
    regexp = "[^<li><a href=].*[^</a></li>]"
    data = re.findall(regexp,str(sections))
    data = data[1:-1]
    cleared = []
    sections = []
    for elem in data:
        if "</a></li>" in elem:
            elem=elem.replace("</a></li>","")
        if '!--' in elem:
            elem=elem.replace('!--<li><a href=',"")
        if '"' in elem:
            elem=elem.replace('"','')
        if "-->" in elem:
            elem = elem.replace("-->","")
            elem=elem.replace("!--","")
        if '  <li><a href=' in elem:
            elem = elem.replace('  <li><a href=','')
        if '!-- <li><a href=' in elem:
            elem =elem.replace('!-- <li><a href=','')
        if 'sub'in elem:
            continue
        cleared.append(elem)
    cleared = list(set(cleared))
    for line in cleared:
        try:
            link, name = line.split(">")
            name = name.replace(r"\n","")
            sections.append(tuple([link[:-1],name[:-1]]))
        except Exception:
            print(line)
    #print(sections)
    return sections


def ParceStore77Net_EachSection(link):
    try:
        response = GetDataFromURL(link)
    except RecursionError:
        print("Website died")
    except NotOKResponseCode:
        os.sleep(3)
        ParceStore77Net_EachSection(link)

    soup = bs(response,"lxml")
    data = soup.find_all("div",class_="blocks_product_fix_w")
    print(data)
def ParceStore77Net():
    URL = "https://store77.net/"
    sections = ParceStore77Net_Sections(URL)
    for page in sections:
        ParceStore77Net_EachSection(URL + page[0][1:])
        break



def main():
    ParceStore77Net()
if __name__ == "__main__":
    main()
