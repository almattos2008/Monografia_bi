from bs4 import BeautifulSoup
import requests

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
            info = {}
            info['web_site'] = web_site_name
            info['headline'] = news.get_text()
            self.total_array.append(info)

    def call_web_site(self, web_site_name, url, class_navigation, navigation_type):
        self.initiate_beautifull_soup(web_site_name, url)
        for cn in class_navigation:
            self.getClasses(web_site_name, navigation_type, cn)

        return self.total_array
