import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
def trade_spider():
    url = 'https://www.tabroom.com/index/tourn/paradigms.mhtml?category_id=52610&tourn_id=20621'
    source_code = requests.get(url)
    plaintext = source_code.text
    soup = BeautifulSoup(plaintext, features="html.parser")
    counter = 0
    paradigm = ""
    with open('paradigms3.csv', 'w', encoding ='utf8', newline='') as x:
        thewriter = csv.writer(x)
        header =['Paradigms', 'JudgingType']
        thewriter.writerow(header)

        for link in soup.findAll('div', {'class':'paradigm'}):
            for paragraph in link.findAll('p'):
                paradigm += paragraph.text + " "
            if (len(paradigm) > 0):
                info = [paradigm]
                thewriter.writerow(info)
                counter += 1
            paradigm = ""

trade_spider()