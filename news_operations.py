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

        # **Acesso aos sites**
        self.urlG1 = "https://g1.globo.com/"
        self.urlR7 = "https://www.r7.com/"
        self.urlUol = "https://www.uol.com.br/"
        self.urlCnnBrasil = "https://www.cnnbrasil.com.br/"
        self.urlFolha = "https://www.folha.uol.com.br/"
        self.urlVeja = "https://veja.abril.com.br/"
        self.urlYahoo = "https://br.noticias.yahoo.com/"
        self.urlEstadao = "https://www.estadao.com.br/"
        self.urlBbcBrasil = "https://www.bbc.com/portuguese"
        self.urlTerra = "https://www.terra.com.br/noticias/"

        self.responses = {}

        self.responses['G1'] = requests.get(self.urlG1, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['R7'] = requests.get(self.urlR7, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['Uol'] = requests.get(self.urlUol, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['CnnBrasil'] = requests.get(self.urlCnnBrasil, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['Folha'] = requests.get(self.urlFolha, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['Veja'] = requests.get(self.urlVeja, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['Yahoo'] = requests.get(self.urlYahoo, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['Estadao'] = requests.get(self.urlEstadao, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['BbcBrasil'] = requests.get(self.urlBbcBrasil, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        self.responses['Terra'] = requests.get(self.urlTerra, headers={
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

    # **G1**
    def callG1(self):
        g1SpanClassNavigation = ["feed-post-link"]
        for g1a in g1SpanClassNavigation:
            self.getClasses("G1", "a", g1a)

    # **R7**
    def callR7(self):
        r7AClassNavigation = ["r7-flex-title-h1__link", "r7-flex-title-h2__link", "r7-flex-title-h3__link",
                              "r7-flex-title-h4__link", "r7-flex-title-h5__link"]

        for r7a in r7AClassNavigation:
            self.getClasses("R7", "a", r7a)

    # **UOL**
    def callUol(self):
        uolH3ClassNavigation = ["headlineMain__title", "title__element headlineSub__content__title"]
        uolAClassNavigation = ["hyperlink relatedList__related"]

        for uolH3 in uolAClassNavigation:
            self.getClasses("Uol", "h3", uolH3)
        for uolA in uolAClassNavigation:
            self.getClasses("Uol", "a", uolA)
        # bigDF.append(toDataSet(uolNews))

    # **CNN**
    def callCnn(self):
        cnnH2ClassNavigation = ["home__title"]
        cnnH3ClassNavigation = ["home__title"]
        for cnnH2 in cnnH2ClassNavigation:
            self.getClasses("CnnBrasil", "h2", cnnH2)
        for cnnH3 in cnnH3ClassNavigation:
            self.getClasses("CnnBrasil", "h3", cnnH3)

    # **FOLHA**
    def callFolha(self):
        folhaH2ClassNavigation = ["c-main-headline__title", "c-headline__title"]
        for folhaH2 in folhaH2ClassNavigation:
            self.getClasses("Folha", "h2", folhaH2)

    # **VEJA**
    def callVeja(self):
        vejaH2ClassNavigation = ["title"]
        for vejaH2 in vejaH2ClassNavigation:
            self.getClasses("Veja", "h2", vejaH2)

    # **YAHOO**
    def callYahoo(self):
        yahooUClassNavigation = ["StretchedBox"]
        yahooH2ClassNavigation = [
            "M(0) Mend(9px) Mt(4px) Fz(12px) LineClamp(2,2.6em) LineClamp(3,4em)--md1100 T(70%) Start(2px) Td(u):h"]
        yahooH3ClassNavigation = ["Mt(0) Td(u):h Mb(13px) Fz(24px)!--miw1100 Fz(18px) LineClamp(4,5.3em) Lh(1.15)"]

        for yahooU in yahooUClassNavigation:
            self.getClasses("Yahoo", "u", yahooU)
        for yahooH2 in yahooH2ClassNavigation:
            self.getClasses("Yahoo", "h2", yahooH2)

    # **ESTADÃO**
    def callEstadao(self):
        # h3 -> a (O link não tem classe, tem que encontrar os links por seu pai (h3))
        estadaoH3ClassNavigation = ["title"]

        for news in self.parsedHtml['Estadao'].find_all("h3"):
            self.constructDict("Estadão", news.find_all("a"))

    # **BBC**
    def callBbc(self):
        # procurar span  dentro do a com a classe abaixo
        bbcAClassNavigation = ["bbc-1fxtbkn evnt13t0"]

        bbcNews = []
        for news in self.parsedHtml['BbcBrasil'].find_all("h3"):
            self.constructDict("BBC", news.find_all("span"))

    # **TERRA**
    def callTerra(self):
        terraAClassNavigation = ["card-news__text--title main-url", "card-h-small__text--title main-url"]
        for terraA in terraAClassNavigation:
            self.getClasses("Terra", "a", terraA)

    # **Busca site a site**
    def callAllSites(self):
        self.callG1()
        self.callR7()
        self.callUol()
        self.callCnn()
        self.callFolha()
        self.callVeja()
        # self.callYahoo()
        self.callEstadao()
        self.callBbc()
        self.callTerra()
        return self.totalArray
