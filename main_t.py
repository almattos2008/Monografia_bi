import openpyxl as openpyxl
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import date
# from google.colab import files
import os.path

# **Acesso aos sites**
urlG1 = "https://g1.globo.com/"
urlR7 = "https://www.r7.com/"
urlUol = "https://www.uol.com.br/"
urlCnnBrasil = "https://www.cnnbrasil.com.br/"
urlFolha = "https://www.folha.uol.com.br/"
urlVeja = "https://veja.abril.com.br/"
urlYahoo = "https://br.noticias.yahoo.com/"
urlEstadao = "https://www.estadao.com.br/"
urlBbcBrasil = "https://www.bbc.com/portuguese"
urlTerra = "https://www.terra.com.br/noticias/"

responses = {}

responses['G1'] = requests.get(urlG1, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['R7'] = requests.get(urlR7, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['Uol'] = requests.get(urlUol, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['CnnBrasil'] = requests.get(urlCnnBrasil, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['Folha'] = requests.get(urlFolha, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['Veja'] = requests.get(urlVeja, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['Yahoo'] = requests.get(urlYahoo, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['Estadao'] = requests.get(urlEstadao, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['BbcBrasil'] = requests.get(urlBbcBrasil, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
responses['Terra'] = requests.get(urlTerra, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})

parsedHtml = {}
for portalName in responses:
    print(str(responses[portalName].status_code) + " " + portalName)
    parsedHtml[portalName] = BeautifulSoup(responses[portalName].text, "html.parser")


# **Carregamento do arquivo em .xlsx**
def selectPreviowsDataFrame():
  if os.path.isfile("base_noticias.xlsx"):
    previousDf = pd.read_excel("base_noticias.xlsx")
    return previousDf
  else:
    previousDf = pd.DataFrame({'date':[], 'site':[], 'news':[]})
    return previousDf

# **Definição do dia atual**
today = date.today()

# dd/mm/YY
totalArray=[]

d1 = today.strftime("%d/%m/%Y")

# **Construção do dicionário**
def getClasses(siteName, navigationType, classes):
    parsed = parsedHtml[siteName].find_all(navigationType, {"class": classes})
    constructDict(siteName, parsed)

def constructDict(siteName, parsed):
  for news in parsed:
    info = {}
    info['date']=d1
    info['site']=siteName
    info['news']=news.get_text()
    totalArray.append(info)

# **Construção do DataFrame**
def toDataSet(newsArray):
  siteDf = pd.DataFrame.from_dict(newsArray)
  return siteDf
  # print(df)

# **Comparação entre o arquivo e o acesso atual**
def compare(siteDf):
  dfN = previousDf.merge(siteDf,indicator=True, how='right')
  dfN = dfN[dfN._merge != 'both']
  dfN.pop('_merge')
  return dfN

# **Montagem do DataFrame com informações novas**
def append(differenceDf):
  newDf = previousDf.append(differenceDf)
  return newDf

# **G1**
def callG1():
  g1SpanClassNavigation = ["feed-post-link"]
  for g1a in g1SpanClassNavigation:
    getClasses("G1", "a" , g1a)

# **R7**
def callR7():
  r7AClassNavigation = ["r7-flex-title-h1__link", "r7-flex-title-h2__link","r7-flex-title-h3__link", "r7-flex-title-h4__link","r7-flex-title-h5__link"]

  for r7a in r7AClassNavigation:
   getClasses("R7", "a" , r7a)

# **UOL**
def callUol():
  uolH3ClassNavigation = ["headlineMain__title", "title__element headlineSub__content__title"]
  uolAClassNavigation = ["hyperlink relatedList__related"]

  for uolH3 in uolAClassNavigation:
    getClasses("Uol", "h3" , uolH3)
  for uolA in uolAClassNavigation:
    getClasses("Uol", "a" , uolA)
  # bigDF.append(toDataSet(uolNews))

# **CNN**
def callCnn():
  cnnH2ClassNavigation = ["home__title"]
  cnnH3ClassNavigation = ["home__title"]
  for cnnH2 in cnnH2ClassNavigation:
    getClasses("CnnBrasil", "h2" , cnnH2)
  for cnnH3 in cnnH3ClassNavigation:
    getClasses("CnnBrasil", "h3" , cnnH3)

# **FOLHA**
def callFolha():
  folhaH2ClassNavigation = ["c-main-headline__title", "c-headline__title"]
  for folhaH2 in folhaH2ClassNavigation:
    getClasses("Folha", "h2" , folhaH2)

# **VEJA**
def callVeja():
  vejaH2ClassNavigation = ["title"]
  for vejaH2 in vejaH2ClassNavigation:
    getClasses("Veja", "h2" , vejaH2)

# **YAHOO**
def callYahoo():
  yahooUClassNavigation = ["StretchedBox"]
  yahooH2ClassNavigation = ["M(0) Mend(9px) Mt(4px) Fz(12px) LineClamp(2,2.6em) LineClamp(3,4em)--md1100 T(70%) Start(2px) Td(u):h"]
  yahooH3ClassNavigation = ["Mt(0) Td(u):h Mb(13px) Fz(24px)!--miw1100 Fz(18px) LineClamp(4,5.3em) Lh(1.15)"]

  for yahooU in yahooUClassNavigation:
    getClasses("Yahoo", "u" , yahooU)
  for yahooH2 in yahooH2ClassNavigation:
    getClasses("Yahoo", "h2" , yahooH2)

# **ESTADÃO**
def callEstadao():
    # h3 -> a (O link não tem classe, tem que encontrar os links por seu pai (h3))
    estadaoH3ClassNavigation = ["title"]

    for news in parsedHtml['Estadao'].find_all("h3"):
        constructDict("Estadão", news.find_all("a"))


# **BBC**
def callBbc():
    # procurar span  dentro do a com a classe abaixo
    bbcAClassNavigation = ["bbc-1fxtbkn evnt13t0"]

    bbcNews = []
    for news in parsedHtml['BbcBrasil'].find_all("h3"):
        constructDict("BBC", news.find_all("span"))

# **TERRA**
def callTerra():
  terraAClassNavigation = ["card-news__text--title main-url", "card-h-small__text--title main-url"]
  for terraA in terraAClassNavigation:
    getClasses("Terra", "a" , terraA)

# **Busca site a site**
def callAllSites():
    callG1()
    callR7()
    callUol()
    callCnn()
    callFolha()
    callVeja()
    # callYahoo()
    callEstadao()
    callBbc()
    callTerra()

# **Chamada principal da aplicação**
callAllSites()
previousDf = selectPreviowsDataFrame()
# print(previousDf.tose)
newNews = compare(toDataSet(totalArray))
print("New News")
print(newNews)
mixedNews = append(newNews)
mixedNews = mixedNews.sort_values(by=['site', 'date'])
print(mixedNews)

# **Salvar em Excel e limpar o array**
mixedNews.to_excel("base_noticias.xlsx",
# header=0,
index=False
)
totalArray.clear()

# **Download do documento**
# files.download('base_noticias.xlsx')

# **Ordenamento do dataframe por site e data**
mixedNews = mixedNews.sort_values(by=['site', 'date'])

# **Seleções por data**
# Seleção por data
mixedNews[mixedNews['date'] == '03/02/2022']


# **Seleção por site**
# Seleção por site
mixedNews[mixedNews['site'] == 'BBC']