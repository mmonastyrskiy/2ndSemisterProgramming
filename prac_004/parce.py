import requests as r
from bs4 import BeautifulSoup as bs 
import mysql.connector as conn
import time
import configparser
import logging
import re
from tqdm import tqdm
import sys
import pandas as pd
#import colorama as color 
blacklisted_url = ["https://store77.net/chasy_apple_watch_nike_se"]
goods = []
sys.setrecursionlimit(100)
class NotOKResponseCode(Exception):
    def __init__(self,message):
        self.message = message

CONFIG_FILE = "config.ini"

logging.basicConfig(filename='access.log')
logging.basicConfig(format='%(asctime)s %(message)s')

#color.init(autoreset=True)

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
    try:
        response = r.get(url)
    except Exception:
        raise NotOKResponseCode("Connection died")
    if response.status_code == 200:
        return response.text
    else:
        raise NotOKResponseCode(f"Something is wrong with the url:{url}, page returned code: {response.status_code}")

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
    global blacklisted_url
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



def Insert_to_database(file):
    df.read_excel(file)
    try:
        mydb=conn.connect(host=host,database=dbname,user=login,password=password)
        c = mydb.cursor()
    except Exception as e:
        print(e)
    df = df.reset_index()
    for index, row in df.iterrows():
        c.execute(f"INSERT INTO catalog (art,name,price,brand,category) VALUES ('{row['arts'][1:-2]}','{row['name'][1:-2]}','{str(row['row'][0:-1])}',{row['brand'][1:-2]},{row['cat'][1:-2]})")
        mydb.commit()


def SaveData():
    
    global goods
    arts = [elem[0] for elem in goods]
    name = [elem[1] for elem in goods]
    price = [elem[2] for elem in goods]
    brand = [elem[3] for elem in goods]
    cat = [elem[4] for elem in goods]
    if not path.exists("res.xlsx")
        for i in tqdm(range(0,len(arts))):
            df = pd.DataFrame({"arts":arts,"name":name,"price":price,"brand":brand,"cat":cat})
            df.to_excel("res.xlsx")
            Insert_to_database("res.xlsx")
    else:
        Insert_to_database("res.xlsx")



def ParceStore77Net_EachSection(link):
    print("New line")
    try:
        response = GetDataFromURL(link)
    except RecursionError:
        print("Website died")
        return
    except NotOKResponseCode:
        time.sleep(10)
        ParceStore77Net_EachSection(link)

    soup = bs(response,"lxml")
    data = soup.find_all("a",class_="bp_hover_text_but_cart")
    #print(data)
    data = str(data).split(' onclick="dataLayer.push({')
    #print(data[3])
    parced_data = []
    for elem in data:
        #print(parced_data)
        elems = elem.split("\n")
        property_ = []
        for line in elems:
            if ":" in line:
                property_.append(tuple([re.sub(r"\s+"," ",line.split(":")[0]),re.sub(r"\s+"," ",line.split(":")[1]).split("//")[0]]))
                #print(property_)
        property_ = property_[9:-1]
        try:
            art = property_[2][1]
            name =property_[1][1]
            price = property_[3][1]
            brand = property_[4][1]
            cat = property_[5][1]
            parced_data.append([art,name,price,brand,cat])
        except Exception:
            pass
    global goods
    for position in parced_data:
        goods.append(position)


def ParceStore77Net():
    URL = "https://store77.net/"
    sections = ParceStore77Net_Sections(URL)
    for page in tqdm(sections):
        print(page)
        if URL + page[0][1:] in blacklisted_url:
            continue
        ParceStore77Net_EachSection(URL + page[0][1:])
        time.sleep(3)
    global goods
    print(len(goods))
    SaveData()



def main():
    ParceStore77Net()
if __name__ == "__main__":
    main()
