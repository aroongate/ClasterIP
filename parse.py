import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup as BS
import multiprocessing as mp


raw_data = pd.read_csv("hackathon.csv", delimiter=";")
inn = raw_data["INN"].tolist()
arrOgr = list()
arrIndex = list()
a = 0
for ins in inn:
    a+=1
    print(str(a) + " " + str(ins))
    req = requests.get("https://vbankcenter.ru/contragent/search?searchStr=" + "0" + str(ins))
    ogrn = BS(req.content, 'html.parser').find_all("gweb-copy")[1].text
    req = requests.get("https://vbankcenter.ru/contragent/" + ogrn)
    index = BS(req.content, 'html.parser').find_all('span',
    'absolute left-0 text-center w-full top-6 font-bold text-white text-3xl')[0].text
    arrOgr.append(ogrn)
    arrIndex.append(index)
raw_data.insert(6,'ogrn',arrOgr)
raw_data.insert(7,'index',arrIndex)
raw_data.to_csv("C:\\Users\\User\\Documents\\vs\\export.csv", index=False)