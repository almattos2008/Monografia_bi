import self as self
from sqlalchemy import create_engine, values
import pandas as pd
import sqlalchemy
from sqlalchemy import update
from sqlalchemy import create_engine


class NewsDatabaseAdapter:

    def __init__(self):
        self.sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/news_headlines', pool_recycle=3600)

    def get_stored_news(self, yesterday):
        dbConnection = self.connect()
        frame = pd.read_sql("select web_site, headline  from news where news_date >= '" + yesterday +"'" , dbConnection)
        # frame = pd.read_sql("SELECT DATE_FORMAT(news_date, '%%Y-%%m-%%d') as news_date  from news", dbConnection)
        # pd.set_option('display.expand_frame_repr', False)
        # print(frame)
        self.close(dbConnection)
        return frame

    def get_stored_news_for_prediction(self):
        dbConnection = self.connect()
        frame = pd.read_sql("select headline from news where theme_prediction_roberta is null and theme_prediction_face is null limit 200" , dbConnection)
        self.close(dbConnection)
        return frame


    def update_news(self, news, roberta, face):
        # engine = create_engine('sqlite://', echo=False)
        dbConnection = self.connect()
        sql =  "UPDATE news SET theme_prediction_roberta = \""+roberta+"\", theme_prediction_face = \""+face+"\" WHERE headline = \""+ news + "\""
        # update("news").where("news".headline == news)
        # values(theme_prediction_roberta=roberta, theme_prediction_face=face)
        # dbConnection.
        dbConnection.execute(sql)
        self.close(dbConnection)

    def save_news(self, dataFrame):
        dbConnection = self.connect()
        dataFrame.to_sql("news", dbConnection, if_exists='append', index=False, dtype={'news_date': sqlalchemy.DateTime()})
        self.close(dbConnection)

    def connect(self):
        dbConnection = self.sqlEngine.connect()
        return dbConnection

    def close(self, dbConnection):
        dbConnection.close()