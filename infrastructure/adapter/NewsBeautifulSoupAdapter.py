from bs4 import BeautifulSoup
import requests
from nltk import word_tokenize


class NewsBeautifulSoupAdapter:

    def __init__(self):
        self.total_array = []
        self.parsedHtml = {}

    def initiate_beautifull_soup(self, web_site_name, url):
        # **Acesso aos sites**
        self.web_url = url

        self.responses = {}

        self.responses[web_site_name] = requests.get(self.web_url, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})

        for portalName in self.responses:
            print(str(self.responses[portalName].status_code) + " " + portalName)
            self.parsedHtml[portalName] = BeautifulSoup(self.responses[portalName].text, "html.parser")

    def getClasses(self, web_site_name, navigation_type, classes):
        parsed = self.parsedHtml[web_site_name].find_all(navigation_type, {"class": classes})
        self.construct_dict(web_site_name, parsed)

    def construct_dict(self, web_site_name, parsed):
        for news in parsed:
            word_tokens = word_tokenize(news.get_text())
            if len(word_tokens) >= 5:
                treated_news = news.get_text().replace('"', '')
                treated_news = news.get_text().replace('  ', '')
                treated_news = treated_news.replace('%', '')
                treated_news = treated_news.replace('</br>', '')
                info = {}
                info['web_site'] = web_site_name
                info['headline'] = treated_news
                self.total_array.append(info)

    def call_web_site(self, web_site_name, url, class_navigation, navigation_type):
        self.initiate_beautifull_soup(web_site_name, url)
        for cn in class_navigation:
            self.getClasses(web_site_name, navigation_type, cn)

    def call_odd_web_site(self, web_site_name, url, class_navigation, navigation_type):
        self.initiate_beautifull_soup(web_site_name, url)
        for news in self.parsedHtml[web_site_name].find_all(class_navigation):
            self.construct_dict(web_site_name, news.find_all(navigation_type))

    def retrieve_array(self):
        return self.total_array

    def empty_array(self):
        self.total_array = []
