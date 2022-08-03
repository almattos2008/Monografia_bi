from datetime import date, timedelta

import infrastructure.adapter.NewsBeautifulSoupAdapter as bs
import pandas as pd
import infrastructure.adapter.NewsDatabaseAdapter as ndba


class NewsUseCase:

    def __init__(self):
        self.bs_adapter = bs.NewsBeautifulSoupAdapter()
        self.news_db_adapter = ndba.NewsDatabaseAdapter()

    def call_site(self, web_site_name, url, class_navigation, navigation_type):
        test = 'test'
        print(test)

    def call_all_sites(self):
        yesterday = date.today() - timedelta(days=1)
        # G1s
        news_array = self.build_all_sites_array()
        web_sites_dataframes = self.to_dataset(news_array)
        stored_dataframe = self.news_db_adapter.get_stored_news(yesterday.strftime("%Y/%m/%d"))
        diff_dataframe = self.compare(web_sites_dataframes, stored_dataframe)
        diff_dataframe = diff_dataframe.assign(news_date=date.today().strftime("%Y/%m/%d"))
        print("Diferenças: " + str(len(diff_dataframe)))
        self.news_db_adapter.save_news(diff_dataframe)

    def to_dataset(self, newsArray):
        siteDf = pd.DataFrame.from_dict(newsArray)
        return siteDf
        # print(df)

    def compare(self, web_sites_dataframes, stored_dataframe):
        dfN = stored_dataframe.merge(web_sites_dataframes, indicator=True, how='right')
        # print(dfN)
        dfN = dfN[dfN._merge != 'both']
        dfN.pop('_merge')
        return dfN

    def build_all_sites_array(self):
        self.bs_adapter.call_web_site("G1", "https://g1.globo.com/", ["feed-post-link"], "a")
        self.bs_adapter.call_web_site("R7", "https://www.r7.com/", ["r7-flex-title-h1__link", "r7-flex-title-h2__link", "r7-flex-title-h3__link",
                              "r7-flex-title-h4__link", "r7-flex-title-h5__link"], "a")
        self.bs_adapter.call_web_site("Uol", "https://www.uol.com.br/", ["headlineMain__title", "title__element headlineSub__content__title"], "h3")
        self.bs_adapter.call_web_site("Uol", "https://www.uol.com.br/", ["hyperlink relatedList__related"], "a")
        self.bs_adapter.call_web_site("CnnBrasil", "https://www.cnnbrasil.com.br/", ["home__title"], "h2")
        self.bs_adapter.call_web_site("CnnBrasil", "https://www.cnnbrasil.com.br/", ["home__title"], "h3")
        self.bs_adapter.call_web_site("Folha", "https://www.folha.uol.com.br/", ["c-main-headline__title", "c-headline__title"], "h2")
        self.bs_adapter.call_web_site("Veja", "https://veja.abril.com.br/", ["title"], "h2")
        self.bs_adapter.call_web_site("Yahoo", "https://br.noticias.yahoo.com/", ["StretchedBox"], "u")
        self.bs_adapter.call_web_site("Yahoo", "https://br.noticias.yahoo.com/", ["M(0) Mend(9px) Mt(4px) Fz(12px) LineClamp(2,2.6em) LineClamp(3,4em)--md1100 T(70%) Start(2px) Td(u):h"], "h2")
        news_array = self.bs_adapter.call_web_site("Terra", "https://www.terra.com.br/noticias/", ["card-news__text--title main-url", "card-h-small__text--title main-url"], "a")

        return news_array




    def callTerra(self):
        terraAClassNavigation = ["card-news__text--title main-url", "card-h-small__text--title main-url"]
        for terraA in terraAClassNavigation:
            self.getClasses("Terra", "a", terraA)

