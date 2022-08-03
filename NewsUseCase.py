from news_operations import news_operations


class NewsUseCase:

    def __init__(self):
        self.news_op = news_operations()

    def call_site(self, name, url):
        self.news_op.initiate_beautifull_soup(name, url)
        if name == "G1":
            self.callG1()


        # **G1**

    def callG1(self):
        g1SpanClassNavigation = ["feed-post-link"]
        for g1a in g1SpanClassNavigation:
            self.news_op.getClasses("G1", "a", g1a)

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