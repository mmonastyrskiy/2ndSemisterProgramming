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
import urllib3
import os.path as path
from copy import copy
import os
import shutil

URL = "https://store77.net/"

obj_pointer = 0

urllib3.disable_warnings()
#import colorama as color
blacklisted_url = ["https://store77.net/chasy_apple_watch_nike_se"]
goods = []
links = []

sys.setrecursionlimit(100)


class NotOKResponseCode(Exception):

    def __init__(self, message):
        self.message = message


CONFIG_FILE = "config.ini"

logging.basicConfig(filename='access.log')
logging.basicConfig(format='%(asctime)s %(message)s')

#color.init(autoreset=True)

try:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    host = config.get("DEFAULT", "host")
    dbname = config.get("DEFAULT", "dbname")
    login = config.get("DEFAULT", "login")
    password = config.get("DEFAULT", "password")

except Exception:
    print("Error reading configuration file")


def GetDataFromURL(url: str) -> str:
    try:
        response = r.get(url, verify=False)
    except Exception:
        raise NotOKResponseCode(
            f"Something is wrong with the url:{url}, page returned code: {response.status_code}"
        )
    if response.status_code == 200:
        return response.text
    else:
        raise NotOKResponseCode(
            f"Something is wrong with the url:{url}, page returned code: {response.status_code}"
        )


def ParceStore77Net_Sections(url):
    try:
        resp = GetDataFromURL(url)
    except NotOKResponseCode:
        print("Seems like host is down, check manually")
    soup = bs(resp, "lxml")
    sections = soup.find_all("ul", class_="catalog_menu_sub_third")
    #print(sections)
    regexp = "[^<li><a href=].*[^</a></li>]"
    data = re.findall(regexp, str(sections))
    data = data[1:-1]
    cleared = []
    sections = []
    global blacklisted_url
    for elem in data:
        if "</a></li>" in elem:
            elem = elem.replace("</a></li>", "")
        if '!--' in elem:
            elem = elem.replace('!--<li><a href=', "")
        if '"' in elem:
            elem = elem.replace('"', '')
        if "-->" in elem:
            elem = elem.replace("-->", "")
            elem = elem.replace("!--", "")
        if '  <li><a href=' in elem:
            elem = elem.replace('  <li><a href=', '')
        if '!-- <li><a href=' in elem:
            elem = elem.replace('!-- <li><a href=', '')
        if 'sub' in elem:
            continue
        cleared.append(elem)
    cleared = list(set(cleared))
    for line in cleared:
        try:
            link, name = line.split(">")
            name = name.replace(r"\n", "")
            sections.append(tuple([link[:-1], name[:-1]]))
        except Exception:
            print(line)
    #print(sections)
    return sections


def ParceStore77Deps(file):
    desc = []
    try:
        df = pd.read_excel(file)
    except Exception as e:
        print(e)
    df = df.reset_index()
    for idx, row in tqdm(df.iterrows()):
        try:
            data = GetDataFromURL(row["link"])
            soup = bs(data, "lxml")
            #print(row['link'])
            global URL
            divs = soup.find_all("div", class_="slick-offer-img-big")
            for div in divs:
                img = div.find("img")
                image_src = img["src"]
                #print(image_src)

        except Exception as e:
            ##print("Image load fail")
            print(e)
        try:
            print(image_src)
            try:
                if not "https" in image_src:
                    image_src = "https://store77.net" + image_src
                response = r.get(image_src, stream=True, verify=False)
            except Exception as e:
                print(e)
            with open(
                    "." + os.sep + "img" + os.sep + str(idx + 1) + "." +
                    image_src.split(".")[-1], "wb") as f:
                shutil.copyfileobj(response.raw, f)
        except Exception:
            print(e)
        try:
            data = GetDataFromURL(row["link"])
        except Exception:
            print(e)
        #print(row["link"])
        soup = bs(data, "lxml")
        Description = soup.find("div", class_="col-sm-6 wrap_descr_b")
        Description = str(Description)
        Description = Description.replace('<div class="col-sm-6 wrap_descr_b>',
                                          "")
        Description = Description.replace("</div>", "")
        desc.append(Description)
    df = pd.read_excel("res.xlsx")
    df["D"] = desc
    df.to_excel("res.xlsx")


def Insert_to_database(file, full=False):
    df = pd.read_excel(file)
    try:
        mydb = conn.connect(host=host,
                            database=dbname,
                            user=login,
                            password=password)
        c = mydb.cursor()
    except Exception as e:
        print(e)
    df = df.reset_index()
    for index, row in tqdm(df.iterrows()):
        article = "".join(row['arts'])
        name = "".join(row['name'])
        price = "".join(str(row['price']))
        brand = "".join(row['brand'])
        category = "".join(row['cat'])
        link = "".join(row['link'])
        Description = "".join(row['D'])

        if not full:
            req_str = f"INSERT INTO catalog (art,name,price,brand,category,links) VALUES ('{article[1:-2]}','{name[1:-2]}','{str(price)[:-2]}','{brand[1:-2]}','{category[1:-2]}','{link}')"
            print(req_str)
            try:
                c.execute(req_str)
            except Exception as e:
                print(e)
            mydb.commit()
        else:
            req_str = f"INSERT INTO catalog (art,name,price,brand,category,links,descr) VALUES ({article[1:-2]},{name[1:-2]},'{str(price)[:-2]}',{brand[1:-2]},{category[1:-2]},'{link}','{str(Description)}')"
            print(req_str)
            try:
                c.execute(req_str)
            except Exception as e:
                print(e)
            mydb.commit()


def SaveData():

    global goods
    arts = [elem[0] for elem in goods]
    name = [elem[1] for elem in goods]
    price = [elem[2] for elem in goods]
    brand = [elem[3] for elem in goods]
    cat = [elem[4] for elem in goods]
    dlink = [elem[-1] for elem in goods]
    if not path.exists("res.xlsx"):
        for i in tqdm(range(0, len(arts))):
            df = pd.DataFrame({
                "arts": arts,
                "name": name,
                "price": price,
                "brand": brand,
                "cat": cat,
                "link": dlink
            })
            df.to_excel("res.xlsx")
            #Insert_to_database("res.xlsx")


def ParceStore77Net_EachSection(link):
    #print("New line")
    parced_links = []
    l = copy(link)
    try:
        response = GetDataFromURL(link + "/")
    except RecursionError:
        print("Website died")
        return
    except NotOKResponseCode:
        time.sleep(10)
        ParceStore77Net_EachSection(link)

    soup = bs(response, "lxml")
    data = soup.find_all("div", class_="blocks_product_fix_w")
    for div in data:
        link = div.find("a", href=True)
        href = link["href"]
        parced_links.append(href)
    idx = 0
    data = soup.find_all("a", class_="bp_hover_text_but_cart")
    #print(data)
    #print(link)
    global links
    data = str(data).split(' onclick="dataLayer.push({')
    link = data[0]
    #print(data[3])
    parced_data = []
    for elem in data:
        #print(parced_data)
        elems = elem.split("\n")
        property_ = []
        for line in elems:
            if ":" in line:
                property_.append(
                    tuple([
                        re.sub(r"\s+", " ",
                               line.split(":")[0]),
                        re.sub(r"\s+", " ",
                               line.split(":")[1]).split("//")[0]
                    ]))
                #print(property_)
        property_ = property_[9:-1]
        try:
            art = property_[2][1]
            name = property_[1][1]
            price = property_[3][1]
            brand = property_[4][1]
            cat = property_[5][1]
            dlink = parced_links[idx]
            idx += 1
            #print(dlink)
            global URL
            parced_data.append(
                [art, name, price, brand, cat, URL[:-1] + dlink])
        except Exception:
            pass
    global goods
    for position in parced_data:
        goods.append(position)


def ParceStore77Net():
    global URL
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
    ParceStore77Deps("res.xlsx")
    Insert_to_database("res.xlsx", full=True)


def main():
    ParceStore77Net()


if __name__ == "__main__":
    main()
