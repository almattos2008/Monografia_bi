import domain.usecase.NewsUseCase as nuc


class NewsRoutes:

    def __init__(self):
        self.news_uc = nuc.NewsUseCase()

    def call_all_sites(self):
        self.news_uc.call_all_sites()

    def call_all_economics_sites(self):
        self.news_uc.call_all_economic_sites()


nr = NewsRoutes()
nr.call_all_sites()
nr.call_all_economics_sites()