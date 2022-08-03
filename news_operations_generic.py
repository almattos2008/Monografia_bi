import openpyxl as openpyxl
import requests
import identification
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import date
# from google.colab import files
import os.path
import mysql.connector


# import database_connection

# print(pd.read_sql(database_connection.connect()))

class news_operations:

    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',
                                             database='news_headlines',
                                             user='root',
                                             password='')



    def initiate_beautifull_soup(self, name, url):
        # **Acesso aos sites**
        self.web_url = url

        self.responses = {}

        self.responses[name] = requests.get(self.web_url, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})

        self.parsedHtml = {}
        for portalName in self.responses:
            print(str(self.responses[portalName].status_code) + " " + portalName)
            self.parsedHtml[portalName] = BeautifulSoup(self.responses[portalName].text, "html.parser")

        # dd/mm/YY
        self.totalArray = []

    # **Construção do dicionário**
    def getClasses(self, siteName, navigationType, classes):
        parsed = self.parsedHtml[siteName].find_all(navigationType, {"class": classes})
        self.constructDict(siteName, parsed)

    def constructDict(self, siteName, parsed):
        for news in parsed:
            info = {}
            info['web_site'] = siteName
            info['headline'] = news.get_text()
            # info['theme_prediction'] = ""
            # info['?theme'] = theme
            self.totalArray.append(info)

    # **Construção do DataFrame**
    def toDataSet(self, newsArray):
        siteDf = pd.DataFrame.from_dict(newsArray)
        return siteDf
        # print(df)

    # **Comparação entre o arquivo e o acesso atual**
    def compare(self, siteDf, previousDf):
        dfN = previousDf.merge(siteDf, indicator=True, how='right')
        # print(dfN)
        dfN = dfN[dfN._merge != 'both']
        dfN.pop('_merge')
        return dfN



    # **Busca site a site**
    def call_web_site(self, name, url):
        self.initiate_beautifull_soup(name, url)


        return self.totalArray
