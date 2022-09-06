class News:
    def __init__(self, web_site,headline,theme,news_date,theme_prediction_face,theme_prediction_roberta):
        self.web_site = web_site
        self.headline = headline
        self.theme = theme
        self.news_date = news_date
        self.theme_prediction_face = theme_prediction_face
        self.theme_prediction_roberta = theme_prediction_roberta